"""
Created on 28/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
"""
from flask import Flask
from flask.ext.admin import Admin
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)