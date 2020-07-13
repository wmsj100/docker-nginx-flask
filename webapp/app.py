#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020  <@57ecb7a85357>
#
# Distributed under terms of the MIT license.

"""

"""
from flask import Flask, Response, render_template_string, render_template, escape, url_for, request
import pymysql
import json

app=Flask(__name__)

class DbOperate(object):
    def __init__(self):
        db = pymysql.connect(host='mysql', 
                port=3306,
                user='root',
                password='123456',
                db='webapp',
                charset='utf8')

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

@app.route('/webapp_user/<username>')
def show_user_profile(username):
	return 'User is {}'.format(escape(username))

@app.route('/post/<int:post_id>')
def show_post_id(post_id):
    return 'Post id is %d' % post_id

@app.route('/path/<path:subpath>')
def show_path(subpath):
    return 'Path is %s' % escape(subpath)

@app.route('/projects/')
def show_projects():
    return "Projects"

@app.route('/about')
def show_about():
    return "About"

@app.route('/url_for/<string:str>')
def show_url_for(str):
    if str == "about":
        return url_for('show_about')
    elif "projects" == str:
        return url_for('show_projects')
    elif "path" == str:
        return url_for('show_path', subpath='aa/bb/cc')
    elif "user" == str:
        return url_for('show_user_profile', username='wmsj100')
    elif "api" == str:
        return url_for('api')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST login"
    elif request.method == 'GET':
        print("method is get\n")
        url_for('static', filename='style.css')
        return "GET login"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
