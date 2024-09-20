from flask import Flask, render_template, request, redirect, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="12345678",  
    database="tip_project"
)
cursor = db.cursor() # database connect

@app.route('/')
def index():
    return render_template('register.html') # index file return

@app.route('/register', methods=['POST'])
def register():
    child_name = request.form['child_name']    #get data using post method
    age = request.form['age']
    parent_name = request.form['parent_name']
    mobile_number = request.form['mobile_number']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Match both password
    if password != confirm_password:   
        flash('Passwords do not match!', 'error')
        return redirect('/')

    # Encrypt password
    hashed_password = generate_password_hash(password)

    # Insert data into MySQL
    try:
        cursor.execute('''INSERT INTO users (child_name, age, parent_name, mobile_number, email, password) 
                          VALUES (%s, %s, %s, %s, %s, %s)''',
                       (child_name, age, parent_name, mobile_number, email, hashed_password))
        db.commit()
        flash('Registration Successful!', 'success')
        return redirect('/')
    except mysql.connector.Error as err:
        flash(f"Error: {err}", 'error')
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
