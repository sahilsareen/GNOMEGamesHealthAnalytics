# Copyright (C) 2016 Sahil Sareen (ssareen [AT] gnome [DOT] org)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version. See http://www.gnu.org/copyleft/gpl.html the full text of the
# license.

# Given the contents of a GNOME project's config file as a string
# Return the dependencies needed by the project as specified there

# Example:
# For gnome-chess:
# ['gio-2.0', 'glib-2.0', 'gmodule-2.0', 'gtk+-3.0', 'librsvg-2.0']

# TODO: Make sure there are no duplicate dependencies
# TODO: Add unit tests


class DependencyExtractor:
    def __init__(self, config_content):
        self.lines = config_content.splitlines()
        self.num_lines = len(self.lines)
        self.dependencies = []

    def get_all(self):
        done = False
        curr_line = 0

        while done is False and curr_line < self.num_lines:
            # Pull out the modules this game depends on
            if self.lines[curr_line].strip().startswith("PKG_CHECK_MODULES"):
                curr_line += 1

                while not self.lines[curr_line].strip().startswith("])"):
                    self.dependencies.append(self.lines[curr_line].strip().split()[0])
                    curr_line += 1
                    done = True
            curr_line += 1

        return self.dependencies
