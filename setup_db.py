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
    ("What will be the output of `bool([])` in Python?", "True", "False", "Error", "None", "B"),
    ("Which of the following is **not** a valid way to declare a dictionary?", 
        "`dict = {}`", "`dict = []`", "`dict = dict()`", "`dict = {'a': 1}`", "B"),
    ("What does `list(map(lambda x: x**2, [1, 2, 3]))` return?", 
        "`[1, 2, 3]`", "`[1, 4, 9]`", "`[1, 8, 27]`", "`None`", "B"),
    ("What is the difference between `is` and `==` in Python?", 
        "`is` checks memory location, `==` checks value", "`is` is the same as `==`", 
        "`==` checks memory location, `is` checks value", "No difference", "A"),
    ("Which of the following Python data structures is immutable?", 
        "`List`", "`Set`", "`Dictionary`", "`Tuple`", "D"),
    ("What will `print(type(lambda x: x))` output?", 
        "`<class 'lambda'>`", "`<class 'function'>`", "`<class 'generator'>`", "`SyntaxError`", "B"),
    ("Which method is used to remove an item from a set?", 
        "`pop()`", "`delete()`", "`remove()`", "`discard()`", "C"),
    ("What does `zip([1, 2], [3, 4])` return?", 
        "`[(1, 3), (2, 4)]`", "`{1: 3, 2: 4}`", "`zip object`", "`None`", "C"),
    ("What will `sorted([3, 1, 4, 1, 5], reverse=True)[-1]` return?", 
        "`5`", "`1`", "`3`", "`Error`", "B"),
    ("Which of the following statements about Python generators is true?", 
        "`They use less memory`", "`They return a list`", 
        "`They store all values in memory`", "`They don't exist in Python`", "A"),
])
    conn.commit()
    print("✅ Sample questions inserted successfully.")
else:
    print("⚠️ Database already contains questions.")

# Close connection
conn.close()
