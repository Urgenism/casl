from flask import render_template,request, flash
from flask_login import login_required, current_user, login_user
from database.database import load_user
from .queries import update_user
import mysql.connector  

from flask import Blueprint

# Create a new blueprint for the games
common = Blueprint('common', __name__)

@common.route('/profile',  methods=['GET', 'POST'])
@login_required
def profile():
    user = current_user
    if request.method == 'POST':
        full_name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        class_id = request.form['class_id']

        try:
            updated_user = update_user(user.id, full_name, email, phone, class_id)
            flash('Update successful', 'success')
            login_user(load_user(user.id))
            user = updated_user
        
        except mysql.connector.IntegrityError:
            flash('Email already exists', 'error')

    if user.role == 'student':
        base_template = 'dashboard-base.html'
    elif user.role == 'teacher':
        base_template = 'dashboard-teacher.html'
    else:
        base_template = 'dashboard-base.html'
        
    return render_template('profile.html', user=user, base_template=base_template)

