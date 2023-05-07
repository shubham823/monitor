# app/views.py

from flask import render_template, redirect, url_for, request
from flask_ldap3_login.forms import LDAPLoginForm
from flask_login import login_user, logout_user, login_required
from ldap3.core.exceptions import LDAPBindError

from . import app, ldap_manager, login_manager
from .models import User

@ldap_manager.save_user
def save_user(dn, username, data, memberships):
    user = User(dn, username)
    return user

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LDAPLoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        try:
            user = ldap_manager.authenticate(username, password)
        except LDAPBindError:
            return render_template('login.html', form=form, error='Invalid username or password')

        if user:
            login_user(user)
           
