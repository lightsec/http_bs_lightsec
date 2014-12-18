'''
Created on 29/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
'''

from httplightsec.app import db
from httplightsec.models import Sensor
from lightsec.store.secrets import AbstractSecretStore


class SQLAlchemySecretStore(AbstractSecretStore):
    # we can "install" it using the admin panel
    def install_auth_secret(self, identifier, secret):
        pass

    # we can "install" it using the admin panel
    def install_enc_secret(self, identifier, secret):
        pass

    def get_auth_secret(self, identifier):
        u = db.session.query(Sensor).filter(Sensor.mac == identifier).first()
        if u is not None:
            return str(u.auth_key)  # expects str not unicode
        return None  # I prefer to make it explicit :-)

    def get_enc_secret(self, identifier):
        u = db.session.query(Sensor).filter(Sensor.mac == identifier).first()
        if u is not None:
            return str(u.enc_key)  # expects str not unicode
        return None  # I prefer to make it explicit :-)