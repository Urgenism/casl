from flask_login import UserMixin
from modules.auth.queries import get_user_by_username, get_user_by_id, create_user

class User(UserMixin):
    def __init__(self, id, username, email, password_hash):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash

    @staticmethod
    def get_by_username(username):
        user_row = get_user_by_username(username)
        if user_row:
            return User(user_row['id'], user_row['username'], user_row['email'], user_row['password_hash'])
        return None

    @staticmethod
    def get_by_id(user_id):
        user_row = get_user_by_id(user_id)
        if user_row:
            return User(user_row['id'], user_row['username'], user_row['email'], user_row['password_hash'])
        return None

    @staticmethod
    def create(username, email, password_hash):
        create_user(username, email, password_hash)
