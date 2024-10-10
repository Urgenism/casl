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

def save_result(user_id, game_id, score):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute('''
        INSERT INTO result (id_user, id_game, score)
        VALUES (%s, %s, %s)
    ''', (user_id, game_id, score))
    result_id = cursor.lastrowid
    
    connection.commit()
    connection.close()
    
    return result_id 