import sqlite3
import random

from calendarDS import calendarDS

class staffDS:
    def __init__(self):
        self.connection = sqlite3.connect('shifts.sqlite3')
        self.cursor = self.connection.cursor()
        self.createTable()
    
    def createTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS staff(
                stuID INTEGER PRIMARY KEY NOT NULL,
                stuName TEXT NOT NULL,
            )   
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS shiftCount(
                stuID INTEGER PRIMARY KEY NOT NULL,
                FOREIGN KEY (stuID) REFERENCES staff(stuID),
                ph1 TEXT NOT NULL,
                nh1 TEXT NOT NULL,
                ph2 TEXT NOT NULL,
                nh2 TEXT NOT NULL,
                backup TEXT NOT NULL
            )   
        ''')


    
    def getShiftTypeCount(self, stuID, shiftType):
        '''
        Returns an int repsenting the frequency of a staff's frequency of shift based off a shiftType

        :param: stuID: ID representing the staff
        :param: shfitType: A string representing the shift type
        '''
        query = f'SELECT {shiftType} FROM shiftCount WHERE stuID = ?'
        self.cursor.execute(query, (stuID))
        shiftNum = self.cursor.fetchall()
        print(shiftNum)
        if (len(shiftNum) != 1):
            return None
        return int(shiftNum)

    def fillPrioDayList(self, numDays):

        listOfDaysOff = {}
            
        self.cursor.execute('SELECT ')

        listOfDaysOff = sorted(listOfDaysOff.items(), key=lambda entry: entry[1], reverse=True)
        return listOfDaysOff

    def sublistBasedShiftType(self, shiftTypeNum, shiftType):
        '''
        Returns a list of singletons that represent the stuIDs for people that have shiftTypeNum shiftTypes
        :param: shiftTypeNum: Frequency of a staff's assigned shifts
        :param: shiftType: A string representing the shift type
        '''
        query = f'SELECT stuID FROM staff WHERE {shiftType} = ?'
        self.cursor.execute(query, (shiftTypeNum))
        return self.cursor.fetchall()
    
    def updateShiftCount(self, shiftType, stuID):
        '''
        Updates the shift count of a certain shift type of an arbitrary staff
        
        :param: shiftType: A string representing the shift type
        :param: stuID: ID representing the staff
        '''
        query = f"UPDATE shiftCount SET {shiftType} = {shiftType} + 1 WHERE stuID = {stuID}"
        self.cursor.execute(query)
        
    def clearTable(self):
        '''
        Deletes all columns in a table
        '''
        self.cursor.execute('DELETE FROM staff')

    def toString(self):
        '''
        Prints a table onto the screen
        '''
        self.cursor.execute('SELECT * FROM staff')
        print(self.cursor.fetchall())
            
# connection = sqlite3.connect('shifts.sqlite3')
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM calendar")
# print(cursor.fetchall())

staff = staffDS()
staff.clearTable()

