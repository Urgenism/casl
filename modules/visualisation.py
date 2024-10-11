import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",      # Your host, 'localhost' for local development
    user="your_username",  # Your MySQL username
    password="your_password",  # Your MySQL password
    database="your_database"   # The database where your student scores are stored
)

# Step 2: Create a cursor to execute SQL queries
cursor = db.cursor()

# Step 3: Write the SQL query to fetch student names and scores
query = "SELECT name, score FROM students"  # Replace 'students' with your table name
cursor.execute(query)

# Step 4: Fetch the data from the database
data = cursor.fetchall()

# Step 5: Close the cursor and connection to free up resources
cursor.close()
db.close()

# Step 6: Process the data into two lists: one for names, one for scores
students = np.array([row[0] for row in data])  # Extract student names
scores = np.array([row[1] for row in data])    # Extract student scores

# Categories based on score levels
levels = []
for score in scores:
    if score < 50:
        levels.append("Average")
    elif 50 <= score <= 75:
        levels.append("Medium")
    else:
        levels.append("Excellent")

# Create a color mapping for each level
color_map = {
    "Average": "red",
    "Medium": "yellow",
    "Excellent": "green"
}
colors = [color_map[level] for level in levels]

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(students, scores, color=colors)

# Add a title and labels
plt.title("Student Performance in Arithmetic Game", fontsize=14)
plt.xlabel("Students", fontsize=12)
plt.ylabel("Scores", fontsize=12)

# Add the score value on top of each bar
for bar, score in zip(bars, scores):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 1, f'{score}', fontsize=12)

# Show the plot
plt.savefig("student_performance.png")
plt.show()
