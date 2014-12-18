"""
Created on 28/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
"""

from werkzeug.security import generate_password_hash
from httplightsec.config import configuration
from httplightsec.app import app, db
from httplightsec.admin import admin
from httplightsec.auth import *
from httplightsec.models import *
from httplightsec.views import *


def create_user_data():
    hashed_passwd = generate_password_hash(configuration.get_password())
    new_user = User(username=configuration.get_username(), password=hashed_passwd)
    db.session.add(new_user)
    return new_user


def create_sensor_data(user):
    new_sensor = Sensor(mac=configuration.get_sensor_mac(), auth_key=configuration.get_auth_key(),
                        enc_key=configuration.get_enc_key(), auth_users=[user])
    db.session.add(new_sensor)


def create_sample_data_if_needed():
    user = db.session.query(User).filter_by(username=configuration.get_username()).first()
    if not user:
        user = create_user_data()

    sensor = db.session.query(Sensor).filter(Sensor.mac == configuration.get_sensor_mac()).first()
    if not sensor:
        create_sensor_data(user)

    db.session.commit()


if __name__ == "__main__":
    db.create_all()
    create_sample_data_if_needed()
    app.run()