from database.database import get_db_connection

def update_user(id, full_name, email, phone, class_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
            UPDATE users
            SET full_name = %s, email = %s, phone = %s, class_id = %s
            WHERE id = %s
        """, (full_name, email, phone, class_id, id))
    
    connection.commit()
    cursor.close()
    connection.close()


def get_user_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user