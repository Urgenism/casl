from flask import render_template
from flask_login import login_required, current_user

from flask import Blueprint

# Create a new blueprint for the dashboard
dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def student():
    return render_template('dashboard.html', user=current_user)

@dashboard.route('/game')
@login_required
def game():
    return render_template('game.html', user=current_user)
