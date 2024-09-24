import os 
from flask import Flask, render_template, redirect, url_for, flash, request, g
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from modules.auth.login import LoginForm
from modules.auth.register import RegistrationForm
from database.init_db import create_tables, close_db
from modules.auth.user import User 
import sass 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'swinburneG22' 

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.before_request
def before_first_request():

    # Compile SCSS to CSS
    scss_dir = os.path.join(os.path.dirname(__file__), 'static/scss')
    css_dir = os.path.join(os.path.dirname(__file__), 'static/css')
    sass.compile(dirname=(scss_dir, css_dir), output_style='compressed')

    # Initialize the database
    create_tables()

# Closing connection on error
@app.teardown_appcontext
def teardown_db(exception):
    close_db()

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

# Routes for authentication, dashboard, and game
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data)
        User.create(form.username.data, form.email.data, password_hash)
        flash('Registration successful. You can now login.')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
