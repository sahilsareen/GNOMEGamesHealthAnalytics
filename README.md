# GNOMEGamesHealthAnalytics
A graph based application to be able to check the health of the GNOME games built using python and neo4j.
- Check which gnome modules builds are failing/passing/timing out/missing from `gnome-continuous` builds
- Find out their dependencies
- Run queries on a graph to find out what possibly broke a module. For example: Find out which dependencies are used exclusively by the failing modules as an indication that the dependency is broken.

[<img src="https://raw.githubusercontent.com/sahilsareen/GNOMEGamesHealthAnalytics/master/GraphExample.png" width=500 height=350 />](https://www.youtube.com/watch?v=OUzUfVo77PI)

* Click on the image above for a demonstration on YouTube.

# Motivation
See my [GNOME blog post](https://blogs.gnome.org/ssareen/2016/01/31/gnome-games-health-analytics/)

# Setup and HowTo

0. Install `python-2.7`

1. Install the following modules using `pip install`: `resources`, `urllib`, `json`, `logging`, `py2neo`

2. Download and install [`Neo4j-Community Edition`](http://neo4j.com/download/)

3. Clone GNOMEGamesHealthAnalytics: `git clone https://github.com/sahilsareen/GNOMEGamesHealthAnalytics.git`

4. Start the Neo4j server

5. Update [GNOMEGamesHealthAnalytics/resources/games.json](https://github.com/sahilsareen/GNOMEGamesHealthAnalytics/blob/master/resources/games.json)
  - Which modules to analyse ?
  - For which date ?

6. Run `cd GNOMEGamesHealthAnalytics/src && python GNOMEGamesHealthAnalysis.py`

# Contributing

1. Generate a pull request
2. Generate patches locally using: `git format-patch -k HEAD~1 --stdout > SomeFix.patch` and email patches to ssareen [AT] gnome [DOT] org

* Stick to the [python style guide](https://www.python.org/dev/peps/pep-0008/)

# License

See [License](https://github.com/sahilsareen/GNOMEGamesHealthAnalytics/blob/master/COPYING)

# Author

- Sahil Sareen (ssareen [AT] gnome [DOT] org)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/sahilsareen/gnomegameshealthanalytics/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

