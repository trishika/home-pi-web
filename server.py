#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
    Home-web
    ~~~~~~~~

    :copyright: (c) 2013 by Aurélien Chabot <aurelien@chabot.fr>
    :license: LGPLv3, see COPYING for more details.
"""
try:
	import sys
	import json
	import urllib2
	from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, _app_ctx_stack
except ImportError as error:
	print 'ImportError: ', str(error)
	exit(1)

try:
	sys.path.insert(0, '../rest/')
	from restClientLib import get_nodes
	from restClientLib import update_sensor
	from restClientLib import set_switch
except ImportError as error:
	print 'Custom py ImportError: ', str(error)
	exit(1)

app = Flask(__name__)

# Server config
if len(sys.argv) > 1:
	fd = open(sys.argv[1])
	servers = json.load(fd)
else:
	print("Not enough argument")
	exit(1)

@app.route('/')
def index():
	switches,sensors = get_nodes(servers)
	
	app.logger.info("switches : %s", switches)
	app.logger.info("sensors : %s", sensors)

	for switch in switches:
		app.logger.info("name : %s", switch["name"])

	for sensor in sensors:
		update_sensor(sensor)
		app.logger.info("name : %s, value: %.1f", sensor["name"], sensor["value"])

	return render_template('index.html', switches=switches, sensors=sensors)

app.run(host="0.0.0.0", port=80, debug=True)
