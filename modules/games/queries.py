from database.database import get_db_connection

def get_games():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM games')
    games = cursor.fetchall()
    cursor.close()
    connection.close()
    return games

def get_questions_by_game_id(game_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    try:
        cursor.execute('SELECT * FROM question WHERE id_game = %s', (game_id,))
        questions = cursor.fetchall()
    except Exception as e:
        print(f"An error occurred: {e}")
        questions = []
    finally:
        cursor.close()
        connection.close()
        
    return questions
