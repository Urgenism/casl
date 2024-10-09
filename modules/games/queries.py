from database.database import get_db_connection

def get_games():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM games')
    games = cursor.fetchall()
    cursor.close()
    connection.close()
    return games

