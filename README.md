
Description
===========

Home-pi-web is part of Home-pi a project aim to
provide domotique service with a raspberrypi.

Home-pi-web is a server providing a web
interface to control stuff through the REST API.

USAGE
=====

Install requirement :

	pip install -r requirements.txt

Run :

	./webServer.py servers.json

Install on the system :

	make install

Dependencies
============

[Flask](http://flask.pocoo.org) : Use to server content.

[Simplejson](https://pypi.python.org/pypi/simplejson/) : Use to easily handle json data.

[Bootstrap](http://twitter.github.io/bootstrap/): Use for web page UI.

Copying
=======

Copyright (C) 2013, Aurélien Chabot <aurelien@chabot.fr>

Licensed under **GPLv3**.

See COPYING file.
