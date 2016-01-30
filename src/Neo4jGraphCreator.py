# Copyright (C) 2016 Sahil Sareen (ssareen [AT] gnome [DOT] org)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version. See http://www.gnu.org/copyleft/gpl.html the full text of the
# license.

from py2neo import Graph, Node, Relationship


class Neo4jGraphCreator:
    def __init__(self):
        self.graph = Graph()
        self.dependency_hash = {}
        self.games_hash = {}
        self.id = 0

    def get_dependency_node(self, dependency_name):
        if dependency_name in self.dependency_hash:
            return self.dependency_hash[dependency_name]

        dependency_node = Node("Dependency", name=dependency_name)
        self.dependency_hash[dependency_name] = dependency_node
        return dependency_node

    def add_game_node(self, game_name):
        # Add it to the cypher commands
        game_node = Node("Game", name=game_name)
        self.games_hash[game_name] = game_node
        self.graph.create(game_node)

    def add_dependency_node(self, game_name, dependency_name):
        # Get the game_id corresponding to the game_name to avoid duplicate nodes
        game_node = self.games_hash[game_name]
        dependency_node = self.get_dependency_node(dependency_name)
        self.graph.create(Relationship(dependency_node, "USED_BY", game_node))

    def generate_game_dependency_graph(self, games_dependencies):
        for game_name, dependencies in games_dependencies.iteritems():
            # Create a game node
            self.add_game_node(game_name)
            # Create dependency nodes
            for dependency in dependencies:
                self.add_dependency_node(game_name, dependency)

    def generate_build_status_graph(self, games, build_status):
        build_pass_node = Node("BuildPassed", name="Build Passed")
        build_fail_node = Node("BuildFailed", name="Build Failed")
        build_timeout_node = Node("BuildTimeout", name="Build Timeout")
        build_missing_node = Node("BuildInfoMissing", name="Build Info Missing")
        for game in games:
            if "success" == build_status[game]:
                self.graph.create(Relationship(self.games_hash[game], "STATUS_IS", build_pass_node))
            elif "failure" == build_status[game]:
                self.graph.create(Relationship(self.games_hash[game], "STATUS_IS", build_fail_node))
            elif "timeout" == build_status[game]:
                self.graph.create(Relationship(self.games_hash[game], "STATUS_IS", build_timeout_node))
            elif build_status[game] is None:
                self.graph.create(Relationship(self.games_hash[game], "STATUS_IS", build_missing_node))

    def build_graph(self, games_dependencies, build_status):
        self.generate_game_dependency_graph(games_dependencies)
        self.generate_build_status_graph(games_dependencies.keys(), build_status)
