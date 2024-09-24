from database.init_db import get_db

def get_user_by_username(username):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    return user

def get_user_by_id(user_id):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    return user

def create_user(username, email, password_hash):
    db = get_db()
    db.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)', 
               (username, email, password_hash))
    db.commit()
