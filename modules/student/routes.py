from flask import render_template, redirect, url_for, session, request, flash
from flask_login import login_required, current_user
from database.database import load_user
from .queries import get_games, get_questions_by_game_id, save_result, get_results_by_user_id
from utils import role_required

from flask import Blueprint

# Create a new blueprint for the games
student = Blueprint('student', __name__)

@student.route('/games')
@login_required
@role_required('student')
def dashboard():
    session.pop('current_question', None)
    session.pop('score', None)
    
    games = get_games()
    return render_template('games.html', user=current_user, games=games)

@student.route('/games/<int:id>',  methods=['GET', 'POST'])
@login_required
@role_required('student')
def question(id):
    questions = get_questions_by_game_id(id)
    
    if 'current_question' not in session:
        session['current_question'] = 0
        session['score'] = 0
    
    current_question_index = session['current_question']
    
    if session['current_question'] >= 10:
        save_result(current_user.id, id, session['score'])
        final_score = session['score']
            
        session.pop('current_question', None)
        session.pop('score', None)
        
        return render_template('question.html', user=current_user, show_result=True, final_score=final_score, game_id=id)
    
    current_question = questions[current_question_index]
    
    if request.method == 'POST':
        
        if request.form.get('action') == 'Skip':
            session['current_question'] += 1
            return redirect(url_for('student.question', id=id))
        
        user_answer = request.form.get('answer')
        
        if not user_answer:
            flash('Please select an option before submitting!', 'error')
            return render_template('question.html', user=current_user, question=current_question, question_no=current_question_index + 1)
        
        if user_answer and int(user_answer) == current_question['correct_answer']:
            session['score'] += 1

        # Move to next question
        session['current_question'] += 1
        
        # Save result
        if session['current_question'] >= 10:
            save_result(current_user.id, id, session['score'])
            final_score = session['score']
             
            session.pop('current_question', None)
            session.pop('score', None)
            
            return render_template('question.html', user=current_user, show_result=True, final_score=final_score, game_id=id)
        
        return redirect(url_for('student.question', id=id))
        
    return render_template('question.html', user=current_user, question=current_question, question_no=current_question_index + 1)


@student.route('/results',  methods=['GET'])
@login_required
@role_required('student')
def results():
    results = get_results_by_user_id(current_user.id)
    print(results)
    return render_template('results.html', user=current_user, results=results)


@student.route('/users',  methods=['GET', 'POST'])
@login_required
def users():
    return render_template('users.html',)

