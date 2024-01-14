import sqlite3

# Connect to the SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object
cursor = conn.cursor()

# Create a table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Insert data into the table
user_data = ('John Doe', 25)
nameer = 'John'
ageer = 25
cursor.execute(f'INSERT INTO users (name, age) VALUES (?, ?)', (nameer, ageer))

# Commit the changes
conn.commit()

# Close the cursor and connection

cursor.execute('SELECT name FROM users WHERE age = 25')
result = cursor.fetchall()
if tuple([nameer]) in result:
    print("nut")

cursor.close()
conn.close()
