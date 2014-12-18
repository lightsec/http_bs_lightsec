"""
Created on 29/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
"""

from flask.ext.login import LoginManager
from httplightsec.app import app


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"