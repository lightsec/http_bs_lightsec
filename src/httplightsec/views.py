'''
Created on 16/11/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
'''

from flask import redirect, request, render_template, url_for
from flask.ext import login as flogin
from flask.ext.admin import helpers
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import login_required, login_user, logout_user
from wtforms import Form, TextField, HiddenField, PasswordField, validators
from werkzeug.security import check_password_hash , generate_password_hash
from httplightsec.app import app, db
from httplightsec.auth import login_manager
from httplightsec.models import User


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

@app.route("/sensors")
@login_required
def show_sensor_keys():
    # locate sensor by id
    #if flogin.current_user.username==:    
    return "bah"