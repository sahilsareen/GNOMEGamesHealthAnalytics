# Copyright (C) 2016 Sahil Sareen (ssareen [AT] gnome [DOT] org)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version. See http://www.gnu.org/copyleft/gpl.html the full text of the
# license.

import sys
import logging

from GamesConfigExtractor import GamesConfigExtractor
from GitHubConfigExtractor import GitHubConfigExtractor
from Neo4jGraphCreator import Neo4jGraphCreator
from BuildStatusChecker import BuildStatusChecker

GAMES_CONFIG_FILE = "../resources/games.json"


class GNOMEGamesHealthAnalytics:
    def __init__(self, config_file=GAMES_CONFIG_FILE):
        self.games_config = GamesConfigExtractor(config_file)

        def get_level():
            return {
                'DEBUG': logging.DEBUG,
                'INFO': logging.INFO,
                'WARN': logging.WARNING,
                'ERROR': logging.ERROR,
                'FATAL': logging.FATAL,
                'CRITICAL': logging.CRITICAL
            }[self.games_config.logging_level]

        logging.basicConfig(format="[%(levelname)s] %(name)s: %(message)s", level=get_level())

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Analysing games health using config in %s" % config_file)

    def run(self):
        games_dependencies = GitHubConfigExtractor().extract_games_config(self.games_config)
        build_status = BuildStatusChecker(self.games_config.build_url).get_status(self.games_config.games)

        # Enable to directly print the Cypher commands to console
        # from CypherGenerator import CypherGenerator
        # neo4j_cypher = CypherGenerator().generate_neo4j_cypher(games_dependencies)
        # for command in neo4j_cypher:
        #    print command

        # Build the graph
        neo4j_graph = Neo4jGraphCreator().build_graph(games_dependencies,build_status)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        GNOMEGamesHealthAnalytics().run()
    elif len(sys.argv) == 2:
        GNOMEGamesHealthAnalytics(sys.argv[1]).run()
    else:
        print("Usage: python GNOMEGamesHealthAnalytics.py [games_config_file_path]")
