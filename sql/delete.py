import sqlite3

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()

cursor.execute('SELECT * FROM Staff')
print(cursor.fetchall())