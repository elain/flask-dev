#!/usr/bin/env python

from flask import Flask
from flask import redirect
from flask import make_response
from flask.ext.script import Manager


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name

@app.route('/re')
def re():
    return redirect('http://www.mi.com')

@app.route('/usr/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello,%s</h1>' % user.name

@app.route('/header')
def header():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response


if __name__ == '__main__':
 #   app.run(debug=True)
    manager.run()

