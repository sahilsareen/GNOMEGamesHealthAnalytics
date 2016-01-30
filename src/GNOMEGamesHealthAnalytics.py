# Copyright (C) 2016 Sahil Sareen (ssareen [AT] gnome [DOT] org)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version. See http://www.gnu.org/copyleft/gpl.html the full text of the
# license.

import sys
from GamesConfigExtractor import GamesConfigExtractor
from GitHubConfigExtractor import GitHubConfigExtractor
from Neo4jGraphCreator import Neo4jGraphCreator

GAMES_CONFIG_FILE = "../resources/games.json"


class GNOMEGamesHealthAnalytics:
    def __init__(self, config_file=GAMES_CONFIG_FILE):
        print("Analysing games health using config in %s" % config_file)
        self.game_config_file = config_file

    def run(self):
        games_config = GamesConfigExtractor(self.game_config_file)
        games_dependencies = GitHubConfigExtractor().extract_games_config(games_config)
        # Enable to directly print the Cypher commands to console
        # from CypherGenerator import CypherGenerator
        # neo4j_cypher = CypherGenerator().generate_neo4j_cypher(games_dependencies)
        # for command in neo4j_cypher:
        #    print command

        # Build the graph
        Neo4jGraphCreator().generate_neo4j_graph(games_dependencies)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        GNOMEGamesHealthAnalytics().run()
    elif len(sys.argv) == 2:
        GNOMEGamesHealthAnalytics(sys.argv[1]).run()
    else:
        print("Usage: python GNOMEGamesHealthAnalytics.py [games_config_file_path]")
