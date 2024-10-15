from flask import Flask
from flask_login import LoginManager
from config import Config
from modules.auth.routes import auth
from modules.student.routes import student
from modules.teacher.routes import teacher
from modules.common.routes import common

import sass
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "Swinburne_G22" 
app.config.from_object(Config)


@app.before_request
def before_first_request():
    # Compile SCSS to CSS
    scss_dir = os.path.join(app.static_folder, 'scss')
    css_dir = os.path.join(app.static_folder, 'css')

    # Compile SCSS files
    try:
        sass.compile(dirname=(scss_dir, css_dir), output_style='compressed')
    except Exception as e:
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
app.register_blueprint(auth)
app.register_blueprint(common)
app.register_blueprint(student)
app.register_blueprint(teacher)

if __name__ == '__main__':
    app.run(port=8000,debug=True)
