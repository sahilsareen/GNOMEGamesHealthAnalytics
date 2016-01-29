# Copyright (C) 2016 Sahil Sareen (ssareen [AT] gnome [DOT] org)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version. See http://www.gnu.org/copyleft/gpl.html the full text of the
# license.

# Pull in the apps config file data from GitHub and extract out the
# dependencies of the app

import requests
from DependencyExtractor import DependencyExtractor


class GitHubConfigExtractor:
    def __init__(self):
        self.session = requests.session()
        self.config = {}

    # Extract the config for a given game
    def extract_config(self, games_name, url):
        req = self.session.get(url)
        return DependencyExtractor(req.content).get_all()

    # Extract the config for all games in the config
    # Returns all the extracted dependencies as a dictionary
    def extract_games_config(self, games_config):
        # The generic url which points to the raw GNOME game config
        # which needs the game name to be put in place
        url = games_config.github_raw_url
        for game_name in games_config.games:
            self.config[game_name] = self.extract_config(game_name, url % game_name)

        return self.config