'''
Created on 29/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
'''

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from httplightsec.app import app, db
from httplightsec.models import Sensor
from httplightsec.views import UserView

admin = Admin(app)  # check /admin
admin.add_view(UserView(db.session))  # , url="user"))
admin.add_view(ModelView(Sensor, db.session))