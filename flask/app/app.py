#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020  <@57ecb7a85357>
#
# Distributed under terms of the MIT license.

"""

"""
from flask import Flask, Response
import json

app=Flask(__name__)

@app.route('/')
def index():
	return "Hello world\n"

@app.route('/api')
def api():
	user = {
		"name" : "wmsj100",
		"age" : 10,
		"sex" : "male"
			}
	return Response(json.dumps(user), mimetype='application/json')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
