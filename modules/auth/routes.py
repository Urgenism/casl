from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from modules.auth.models import User
from .queries import insert_user, get_user_by_email
import mysql.connector  

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        phone = request.form['phone']
        role = request.form['role']
        class_id = request.form['class_id']

        # Validate passwords match
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('auth.register'))

        # Hash password
        hashed_password = generate_password_hash(password)

        try:
            insert_user(full_name, email, hashed_password, phone, role, class_id)
            flash('Registration successful', 'success')
            return redirect(url_for('auth.login'))
        except mysql.connector.IntegrityError:
            flash('Email already exists', 'error')

    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        print(email, password)

        user_data = get_user_by_email(email)
         
        if user_data and check_password_hash(user_data['password'], password):
            user = User(**user_data)
            login_user(user)
            
            if(user_data['role'] == 'student'):
                return redirect(url_for('student.dashboard'))  
            elif(user_data['role'] == 'teacher'):
                return redirect(url_for('teacher.dashboard'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('auth.login'))
