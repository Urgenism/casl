from flask import render_template
from flask_login import login_required, current_user
from .queries import get_games

from flask import Blueprint

# Create a new blueprint for the games
games = Blueprint('games', __name__)

@games.route('/games')
@login_required
def dashboard():
    games = get_games()
    print(games)
    return render_template('games.html', user=current_user, games=games)

@games.route('/games/<int:id>',  methods=['GET'])
@login_required
def game_question(id):
    print(id)
    return render_template('game-question.html', user=current_user)
