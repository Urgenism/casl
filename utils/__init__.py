from functools import wraps
from flask import abort
from flask_login import current_user

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.role != role:
                abort(403)  # Return a 403 Forbidden response
            return func(*args, **kwargs)
        return wrapper
    return decorator
