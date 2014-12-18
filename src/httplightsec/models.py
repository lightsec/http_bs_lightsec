"""
Created on 29/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
"""

from httplightsec.app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)
    has_access_to = db.relationship('Sensor', secondary=lambda: access_table)

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return self.username

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


# new_user = User(...)
#db.session.add(new_user)
#db.session.commit()


class Sensor(db.Model):
    __tablename__ = 'sensor'
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(12), unique=True)
    auth_key = db.Column(db.String(120))
    enc_key = db.Column(db.String(120))
    auth_users = db.relationship('User', secondary=lambda: access_table)
    #auth_user

    def __str__(self):
        return 'Sensor%r' % self.id

    def __repr__(self):
        return '<Sensor %r>' % self.id


access_table = db.Table('access', db.Model.metadata,
                        db.Column('sensor_id', db.Integer, db.ForeignKey('sensor.id')),
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)
