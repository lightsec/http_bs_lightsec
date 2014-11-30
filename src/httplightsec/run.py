'''
Created on 28/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
'''

from httplightsec.app import app, db
from httplightsec.admin import *
from httplightsec.auth import *
from httplightsec.models import *
from httplightsec.views import *


if __name__ == "__main__":
    db.create_all()
    app.run()