# Copyright (C) 2016 Sahil Sareen (ssareen [AT] gnome [DOT] org)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version. See http://www.gnu.org/copyleft/gpl.html the full text of the
# license.

# Read the games configuration from the config file
# present in resources(games.json)
# TODO: Upgrade to typesafe config: https://github.com/chimpler/pyhocon

import json


class GamesConfigExtractor:
    def __init__(self, file_name):
        with open(file_name) as data_file:
            config = json.load(data_file)

        self.games = config["games"]
        self.github_raw_url = config["github_raw_configure"]
        self.build_url = config["build_url"] % config["date"]
        self.logging_level = config["logging_level"]