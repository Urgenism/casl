from flask import render_template
from flask_login import login_required, current_user

from flask import Blueprint

# Create a new blueprint for the dashboard
result = Blueprint('result', __name__)


@result.route('/result')
@login_required
def game():
    return render_template('result.html', user=current_user)