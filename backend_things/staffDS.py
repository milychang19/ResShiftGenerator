import sqlite3

class staffDS:
    def __init__(self):
        self.connection = sqlite3.connect('shifts.sqlite3')
        self.cursor = self.connection.cursor()
    
    def createTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS staff(
                stuID INTEGER NOT NULL,
                stuName TEXT NOT NULL,
                timeOff INTEGER,
                FOREIGN KEY (timeOff) REFRENCES days(dayNum),
                PH1 INTEGER NOT NULL,
                NH1 INTEGER NOT NULL,
                PH2 INTEGER NOT NULL,
                NH2 INTEGER NOT NULL,
                BACKUP INTEGER NOT NULL
            )   
        ''')
    
    
