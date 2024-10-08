from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="12345678",  
    database="tip_project"  
)


@app.route('/results/<int:user_id>')
def results(user_id):

    cursor = db.cursor()
    # give user name
    cursor.execute("SELECT name FROM user WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    # give quiz score
    cursor.execute("SELECT score FROM result WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()

    db.close()

    if user is None or result is None:
        return "User or result not found", 404

    return render_template('results.html', name=user[0], score=result[0])

if __name__ == "__main__":
    app.run(debug=True)