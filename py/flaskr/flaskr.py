#!/usr/bin/python

# all the imports
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,\
     abort,render_template,flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG	= True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

