import sqlite3
from flask import g

DATABASE = 'database/database.db'

# Establish the database connection
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  # Return dict-like row
    return g.db

# Close the database connection when app context ends
def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Initialize the database by reading all schema files
def create_tables():
    db = get_db()
    schema_files = ['database/schema/auth.sql']
    
    for schema_file in schema_files:
        with open(schema_file, 'r') as f:
            db.executescript(f.read())
    db.commit()
