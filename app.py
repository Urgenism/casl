from flask import Flask
from flask_login import LoginManager
from config import Config
from database.database import load_user

import sass  # Import the sass library

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure key in production
app.config.from_object(Config)

# Compile SCSS to CSS
scss_file = 'static/scss/app.scss'
css_file = 'static/css/app.css'

try:
    with open(css_file, 'w') as f:
        f.write(sass.compile(filename=scss_file))
except OSError as e:
    print(f"Error compiling SCSS: {e}")

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Redirect to login if not authenticated

@login_manager.user_loader
def load_user(user_id):
    from database.database import load_user
    return load_user(user_id)

# Register blueprints
from modules.auth.routes import auth
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)
