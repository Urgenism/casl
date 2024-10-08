from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="12345678",  
    database="tip_project"  
)

cursor = db.cursor()

@app.route('/')
def quiz():
    cursor.execute("SELECT * FROM Question")
    questions = cursor.fetchall()
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    cursor.execute("SELECT * FROM Question")
    questions = cursor.fetchall()

    correct_answers = {q[0]: q[3] for q in questions}
    score = 0
    total = len(questions)

    for question in questions:
        qid = str(question[0])
        selected_option = request.form.get(f'question_{qid}')
        if selected_option == correct_answers[qid]:
            score += 1

    
    cursor.execute("INSERT INTO Result (Score, Total) VALUES (%s, %s)", (score, total))
    db.commit()

    return f"Your score is {score} out of {total}."

if __name__ == '__main__':
    app.run(debug=True)
