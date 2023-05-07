# config.py
import os
class Config:
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    DEBUG = True

    # LDAP
    LDAP_HOST = 'your_ldap_host'
    LDAP_PORT = 389
    LDAP_BASE_DN = 'your_ldap_base_dn'
    LDAP_USER_DN = 'your_ldap_user_dn'
    LDAP_USER_SEARCH_SCOPE = 'SUBTREE'

    # Flask-LDAP3Login
    LDAP3LOGIN_USERNAME_ATTR = 'uid'
    LDAP3LOGIN_USER_OBJECT_FILTER = '(objectClass=person)'

    # Flask-Login
    REMEMBER_COOKIE_DURATION = 3600
