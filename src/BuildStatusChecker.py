# Copyright (C) 2016 Sahil Sareen (ssareen [AT] gnome [DOT] org)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version. See http://www.gnu.org/copyleft/gpl.html the full text of the
# license.

import urllib, json


class BuildStatusChecker:
    def __init__(self, url):
        response = urllib.urlopen(url)
        self.data = json.loads(response.read())
        self.build_status = {}

    def get_game_status(self, game):
        for item in self.data["apps"]:
            if item["id"].lower().find(game) is not -1:
                return item["state"]

    def get_status(self, games):
        for game in games:
            self.build_status[game] = self.get_game_status(game)
        return self.build_status
