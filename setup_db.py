import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("quiz.db", check_same_thread=False)
cursor = conn.cursor()

# Create the quiz_questions table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS quiz_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
''')
conn.commit()

# Insert sample questions (Only if the table is empty)
cursor.execute("SELECT COUNT(*) FROM quiz_questions")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany('''
        INSERT INTO quiz_questions (question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', [
        ("What is the output of `print(2**3)`?", "4", "6", "8", "10", "C"),
        ("Which of these is a mutable data type in Python?", "List", "Tuple", "String", "Integer", "A"),
        ("What keyword is used to define a function in Python?", "func", "def", "define", "lambda", "B"),
        ("Which of these is used for loop iteration in Python?", "for", "repeat", "while", "loop", "A"),
        ("How do you start a comment in Python?", "#", "//", "/*", "--", "A")
    ])
    conn.commit()
    print("✅ Sample questions inserted successfully.")
else:
    print("⚠️ Database already contains questions.")

# Close connection
conn.close()
