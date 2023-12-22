import mysql.connector 

#https://medium.com/learning-sql/use-vscode-extension-sqltools-to-format-sql-code-72faad9c8b45#:~:text=Last%20but%20not%20least%2C%20open,for%20an%20early%20coffee%20break!

db = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "EastIsBeast",
    database = "residence_assistants"
    )

staff_list = [("richard", "98765"), 
              ("molin", "23415"), 
              ("emily", "72675")]

staff_shifts = [(4,3),
               (1,5),
               (6,2)]

mycursor = db.cursor()

#mycursor.execute("DROP TABLE IF EXISTS Staff")
# Corrected SQL statement for creating the table
# mycursor.execute("CREATE TABLE Staff (personID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), stuID INT UNSIGNED)")

Q1 = "CREATE TABLE Staff (personID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), stuID INT UNSIGNED)"
Q2 = "CREATE TABLE Shifts (personIndex int PRIMARY KEY, FOREIGN KEY(personIndex) REFERENCES Staff(personID), FH int DEFAULT 0, SH int DEFAULT 0)"

#mycursor.execute(Q1)
#mycursor.execute(Q2)
#mycursor.execute("SHOW TABLES")

Q3 = "INSERT INTO Staff (name, stuID) VALUES (%s, %s)"
#mycursor.executemany("INSERT INTO Staff (name, stuID) VALUES (%s, %s)", staff_list)

Q4 = "INSERT INTO Shifts (personIndex, FH, SH) VALUES (%s, %s, %s)"

# mycursor.execute("INSERT INTO Staff (name, stuID) VALUES (%s, %s)", ("dan", 12345))
# mycursor.execute("INSERT INTO Staff (name, stuID) VALUES (%s, %s)", ("fin", 56732))

# mycursor.execute("SELECT * FROM Staff")

#mycursor.execute("DESCRIBE Staff")
# for x in mycursor:
#     print(x)

# for x, staff in enumerate(staff_list):
#     mycursor.execute(Q3, staff)
#     last_id = mycursor.lastrowid
#     mycursor.execute(Q4, (last_id,) + staff_shifts[x])
#db.commit()

mycursor.execute("SELECT * FROM Staff")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Shifts")
for x in mycursor:
    print(x)

#db.commit()
db.close()



print("Connection created successfully!")