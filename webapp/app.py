#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020  <@57ecb7a85357>
#
# Distributed under terms of the MIT license.

"""

"""
from flask import Flask, Response, render_template_string
import pymysql
import json

app=Flask(__name__)

class DbOperate(object):
    def __init__(self):
        db = pymysql.connect('mysql', 'root', '123456', 'webapp')

@app.route('/')
def index():
	return "Hello world\n"

@app.route('/api')
def api():
    try:
        db = DbOperate()
    except:
        return render_template_string('<h1>Mysql Can not connect</h1>')
    print("ok")
    return render_template_string('<h1>Hello Flask haha www!!!</h1>')
	#return Response(json.dumps(user), mimetype='application/json')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
