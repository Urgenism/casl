from functools import wraps
from flask import abort
from flask_login import current_user

class User:
    def __init__(self, id, full_name, email, phone, role, class_id, active):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.role = role
        self.class_id = class_id
        self.active = active
        

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.role != role:
                abort(403)  # Return a 403 Forbidden response
            return func(*args, **kwargs)
        return wrapper
    return decorator


def dict_to_user(data):
    return User(
        id=data['id'],
        full_name=data['full_name'],
        email=data['email'],
        phone=data['phone'],
        role=data['role'],
        class_id=data['class_id'],
        active=data['active']
    )