from flask import render_template, request
from flask_login import login_required, current_user
from .queries import get_students, udpate_result_by_id
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
    return render_template('student-results.html', user=current_user, students=students )

@teacher.route('/student-results/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
def student_results(id):
    results = get_results_by_user_id(id)
    print(id)
    
    if request.method == 'POST':
        result_id = request.form['result_id']
        feedback = request.form['action']
  
        udpate_result_by_id(result_id, feedback)
                
        results = get_results_by_user_id(id)

    base_template = 'dashboard-teacher.html'
        
    return render_template('results.html', user=current_user, results=results, base_template=base_template )
