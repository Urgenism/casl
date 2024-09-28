from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, full_name, email, password, phone, user_type, class_id):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password = password
        self.phone = phone
        self.user_type = user_type
        self.class_id = class_id

    def get_id(self):
        return str(self.id)
