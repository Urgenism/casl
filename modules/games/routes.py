from flask import render_template, redirect, url_for, session, request, flash
from flask_login import login_required, current_user
from .queries import get_games, get_questions_by_game_id

from flask import Blueprint

# Create a new blueprint for the games
games = Blueprint('games', __name__)

@games.route('/games')
@login_required
def dashboard():
    games = get_games()
    print(games)
    return render_template('games.html', user=current_user, games=games)

@games.route('/games/<int:id>',  methods=['GET', 'POST'])
@login_required
def question(id):
    questions = get_questions_by_game_id(id)
    
    if 'current_question' not in session:
        session['current_question'] = 0
        session['score'] = 0
    
    current_question_index = session['current_question']
    
    if current_question_index >= len(questions):
        return redirect(url_for('games.result'))
    
    current_question = questions[current_question_index]
    
    if request.method == 'POST':
     
        
        if request.form.get('action') == 'Skip':
            session['current_question'] += 1
            return redirect(url_for('games.question', id=id))
        
        user_answer = request.form.get('answer')
        
        if not user_answer:
            # Flash an error message if no answer is selected
            flash('Please select an option before submitting!', 'error')
            return render_template('question.html', user=current_user, question=current_question, question_no=current_question_index + 1)
        
        if user_answer and int(user_answer) == current_question['correct_answer']:
            session['score'] += 1

        # Move to next question
        session['current_question'] += 1
        return redirect(url_for('games.question', id=id))
        
    return render_template('question.html', user=current_user, question=current_question, question_no=current_question_index + 1)


@games.route('/result',  methods=['GET'])
@login_required
def result():
    
    print("your score is", session['score'])
    session['current_question'] = 0
    session['score'] = 0
    
    return render_template('result.html', user=current_user)

