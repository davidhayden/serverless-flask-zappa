import os
from flask_login import UserMixin
from app import login


class User(UserMixin):
    def __init__(self, username):
        self.id = 1
        self.username = username


@login.user_loader
def load_user(id):
    return User(os.getenv('ADMIN_USERNAME'))

def login_valid(username, password):
    return username == os.getenv("ADMIN_USERNAME") and \
        password == os.getenv("ADMIN_PASSWORD")
