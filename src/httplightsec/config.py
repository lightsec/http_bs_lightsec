"""
Created on 18/12/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
"""

import argparse
import ConfigParser


class ConfigFileReader(object):

    def __init__(self, file_path):
        self.config = ConfigParser.RawConfigParser()
        self.config.read(file_path)

    def get_secret(self):
        return self.config.get('App', 'secret')

    def get_database_path(self):
        return self.config.get('App', 'database')

    def get_username(self):
        return self.config.get('User', 'username')

    def get_password(self):
        return self.config.get('User', 'password')

    def get_sensor_mac(self):
        return self.config.get('Sensor', 'mac')

    def get_auth_key(self):
        return self.config.get('Sensor', 'authkey')

    def get_enc_key(self):
        return self.config.get('Sensor', 'enckey')


parser = argparse.ArgumentParser(description='Run sample web server which uses liblightsec.')
parser.add_argument('-config', default='../../config.ini', dest='config',
                    help='Configuration file.')
args = parser.parse_args()
configuration = ConfigFileReader(args.config)