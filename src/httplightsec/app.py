"""
Created on 28/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from httplightsec.config import configuration

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = configuration.get_secret()  # To allow sessions
app.config['SQLALCHEMY_DATABASE_URI'] = configuration.get_database_path()

db = SQLAlchemy(app)