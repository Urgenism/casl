from flask import render_template, request
from flask_login import login_required, current_user
from .queries import get_users, udpate_user_by_id, delete_user_by_id
from utils import role_required

from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/users',  methods=['GET', 'POST'])
@login_required
@role_required('admin')
def users():
    
    if request.method == 'POST':
        user_id = request.form['user_id']
        action = request.form['action']
        
        if action == 'delete':
            delete_user_by_id(user_id) 
        elif action == 'activate':
            udpate_user_by_id(user_id, 1) 
        elif action == 'deactivate':
            udpate_user_by_id(user_id, 0) 
                
    users = get_users()
        
    return render_template('users.html', user=current_user, users=users )
