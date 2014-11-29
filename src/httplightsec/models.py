'''
Created on 29/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
'''
from httplightsec.app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
        # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

#new_user = User(...)
#db.session.add(new_user)
#db.session.commit()