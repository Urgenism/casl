from database.database import get_db_connection

def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return users

def udpate_user_by_id(id, active):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        UPDATE users 
        SET active=%s
        WHERE id=%s
    ''', (active, id))
    
    connection.commit()
    cursor.close()
    connection.close()
    

def delete_user_by_id(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (id,)) 
    connection.commit()
    cursor.close()
    connection.close()