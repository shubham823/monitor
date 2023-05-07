# app/models.py

class User:
    def __init__(self, dn, username):
        self.dn = dn
        self.username = username

    def get_id(self):
        return self.dn

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
