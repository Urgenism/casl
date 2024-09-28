from database.database import get_db_connection

def insert_user(full_name, email, hashed_password, phone, user_type, class_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO users (full_name, email, password, phone, user_type, class_id) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (full_name, email, hashed_password, phone, user_type, class_id))
    connection.commit()
    cursor.close()
    connection.close()

def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user