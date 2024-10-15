from flask import render_template
from flask_login import login_required, current_user
from .queries import get_students
from modules.student.queries import get_results_by_user_id
import mysql.connector  
from utils import role_required

from flask import Blueprint

teacher = Blueprint('teacher', __name__)

@teacher.route('/student-results')
@login_required
@role_required('teacher')
def student_list():
    students = get_students()
    print(students, 'students')
    return render_template('student-results.html', user=current_user, students=students )

@teacher.route('/student-results/<int:id>')
@login_required
@role_required('teacher')
def student_results(id):
    results = get_results_by_user_id(id)
    print(id)
    return render_template('results.html', user=current_user, results=results )
