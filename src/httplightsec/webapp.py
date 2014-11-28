'''
Created on 16/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
'''

from flask import Flask, g, session, redirect, request, render_template, flash, url_for
from flask.ext import login as flogin
from flask.ext.admin import Admin, helpers
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import LoginManager, login_required, login_user, logout_user
from wtforms import Form, TextField, HiddenField, PasswordField, validators
from werkzeug.security import check_password_hash , generate_password_hash


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)

# Create dummy secret key so we can use sessions
app.config['SECRET_KEY'] = 'super dummy s3cret'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#new_user = User(...)
#db.session.add(new_user)
#db.session.commit()


class User(db.Model):
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

class UserView(ModelView):
    
    def __init__(self, db_session, **kwargs):
        super(UserView, self).__init__(User, db_session, **kwargs)
    
    def create_model(self, form):
        form.password.data = generate_password_hash(form.password.data) # let's hash it
        super(UserView, self).create_model(form)
    
    def update_model(self, form, model):
        form.password.data = generate_password_hash(form.password.data) # let's hash it
        super(UserView, self).update_model(form, model)


class LoginForm(Form):
    username = TextField('Username', [
        validators.Required(),
        validators.Length(min=4, max=25)
    ])
    password = PasswordField('New Password', [
        validators.Required()#,
        #validators.EqualTo('confirm', message='Passwords must match')
    ])
    #confirm = PasswordField('Repeat Password')
    next = HiddenField()
        
    def set_next(self, value):
        if value:
            self.next.data = value
    
    def validate_username(self, field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')
    
    def get_user(self):
        return db.session.query(User).filter_by(username=self.username.data).first()
        # user = User.query.filter_by(username=username).first()

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

@app.route("/")
def index():
    return "Hello World!"
    
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    form.set_next(request.args.get("next")) # GET argument to POST
    
    # this page is called twice! (POST /login)
    # In the second call "next" parameter is lost!
    if helpers.validate_form_on_submit(form):
        user = form.get_user()
        flogin.login_user(user)
        #flash("Logged in successfully.")
        
    if flogin.current_user.is_authenticated():
        return redirect(form.next.data or url_for("index"))
    
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    flogin.logout_user()
    return redirect(url_for("index"))

@app.route("/settings")
@login_required
def settings():
    return "Logged!"


if __name__ == "__main__":
    db.create_all()
    admin = Admin(app) # check /admin
    admin.add_view(UserView(db.session)) #, url="user"))
    
    app.run()