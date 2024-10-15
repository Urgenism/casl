from database.database import get_db_connection

def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE role = %s", ("student",))
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students
