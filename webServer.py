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
	from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
except ImportError as error:
	print 'ImportError: ', str(error)
	exit(1)

try:
	sys.path.insert(0, '../rest/')
	sys.path.insert(0, '/usr/local/bin/')
	from restClientLib import get_nodes, set_switch, update_sensor, update_switch
except ImportError as error:
	print 'Custom py ImportError: ', str(error)
	exit(1)

app = Flask(__name__)

# Server config
if len(sys.argv) > 1:
	config = sys.argv[1]
else:
	config = "servers.json"

try:
	fd = open(config)
	servers = json.load(fd)
except:
	print("Invalid configuration file")
	exit(1)

@app.route('/')
def index():
	switches,sensors = get_nodes(servers)

	app.logger.info("switches : %s", switches)
	app.logger.info("sensors : %s", sensors)

	for switch in switches:
		update_switch(switch)
		app.logger.info("name : %s, status: %d", switch["name"], switch["status"])

	for sensor in sensors:
		update_sensor(sensor)
		app.logger.info("name : %s, value: %.1f", sensor["name"], sensor["value"])

	return render_template('index.html', switches=switches, sensors=sensors)

app.run(host="0.0.0.0", port=80, debug=True)
