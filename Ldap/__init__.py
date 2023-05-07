# app/__init__.py

from flask import Flask
from flask_ldap3_login import LDAP3LoginManager
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# CSRF protection
csrf = CSRFProtect(app)

# LDAP3Login and Flask-Login initialization
ldap_manager = LDAP3LoginManager(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import the views and models
from . import views, models
