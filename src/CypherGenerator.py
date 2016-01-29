# Copyright (C) 2016 Sahil Sareen (ssareen [AT] gnome [DOT] org)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version. See http://www.gnu.org/copyleft/gpl.html the full text of the
# license.

# TODO: Directly update Neo4j instead of generating commands

CREATE_GAME_NODE = "CREATE (%s:Game {name: '%s'})"
CREATE_DEPENDENCY = "MERGE (%s:Dependency {name:'%s'})-[:USED_BY]->(%s)"


class CypherGenerator:
    def __init__(self):
        self.cypher_commands = []
        self.dependency_hash = {}
        self.games_hash = {}
        self.id = 0

    def get_identifier(self):
        self.id += 1
        return "var%d" % self.id

    def get_dependency_id(self, dependency_name):
        if dependency_name in self.dependency_hash:
            return self.dependency_hash[dependency_name]

        dependency_id = self.get_identifier()
        self.dependency_hash[dependency_name] = dependency_id
        return dependency_id

    def add_game_node(self, game_name):
        # Add it to the cypher commands
        game_id = self.get_identifier()
        self.games_hash[game_name] = game_id
        self.cypher_commands.append(CREATE_GAME_NODE % (game_id, game_name))

    def add_dependency_node(self, game_name, dependency_name):
        # Get the game_id corresponding to the game_name to avoid duplicate nodes
        game_id = self.games_hash[game_name]
        dependency_id = self.get_dependency_id(dependency_name)
        self.cypher_commands.append(CREATE_DEPENDENCY % (dependency_id, game_name,game_id))

    def generate_neo4j_cypher(self, games_dependencies):
        for game_name, dependencies in games_dependencies.iteritems():
            # Create a game node
            self.add_game_node(game_name)
            # Create dependency nodes
            for dependency in dependencies:
                self.add_dependency_node(game_name, dependency)
        return self.cypher_commands
