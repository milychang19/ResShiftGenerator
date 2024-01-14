import calendar
import sqlite3



class calendarDS:
    def __init__(self, year, month):
        """
        Assigns a employee a specific type of shift

        :param numEmployees: Number of employees we're dealing with. (int)
        :param year: The year in question. (int)
        :param month: The month in question. (int)
        """

        monthTuple = calendar.monthrange(year, month)
        self.startDay = int(monthTuple[0])
        self.numDays = int(monthTuple[1])
        self.connection = sqlite3.connect('shifts.sqlite3')
        self.cursor = self.connection.cursor()
        self.createTable()
    
    def createTable(self):
        self.clearTable()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS calendar(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dayNum INTEGER,
                shiftType TEXT NOT NULL,
                stuID INTEGER NOT NULL
            )
        ''')
    
    def getCalendar(self):
        return self.cursor
    
    def getStartDay(self):
        return self.getStartDay
    
    def getNumDays(self):
        return self.numDays
    
    def getNumEmployees(self):
        return self.numEmployees
    
    def getShiftType(self, dayNum, employeeNum):
        """
        Returns an employee's shift type on a specific day

        :param employeeNum: An index representing the employee. (int)
        :param dayNum: Number representing the day. (int)
        :return: A tuple that only contains a string representing the shift type
        :rtype: singleton
        """
        self.cursor.execute('SELECT shiftType FROM calendar WHERE stuID = ? AND dayNum = ?', (employeeNum, dayNum))
        return self.cursor.fetchone()

    def assignEmployeeShift(self, employeeNum, dayNum, shiftType):
        """
        Assigns a employee a specific type of shift

        :param employeeNum: An index representing the employee. (int)
        :param dayNum: Number representing the day. (int)
        :param shiftTypeNum: Number representing the shift type. (int)
        """
        self.cursor.execute('INSERT INTO calendar (stuID, dayNum, shiftType) VALUES (?, ?, ?)', (employeeNum, dayNum, shiftType))
        self.connection.commit()
    
    def isEmployeeAssigned(self, employeeNum, dayNum):
        '''
        Checks if an employee is assigned or not
        '''
        if self.getShiftType(dayNum, employeeNum) is None:   return False
        else:   return True
    
    def unavailableEmployees(self, dayNum, dayOffSymbol):
        """
        Returns list of employees whom are unavailable for the day

        :param dayNum: Number representing the day.(int)
        :param unavailableNum: The number representing an called off day. (int)
        :return: List of employees whose status matches the unavailableNum
        :rtype: List
        """
        self.cursor.execute('SELECT stuID FROM calendar WHERE dayNum = ? AND shiftType = ?', (dayNum, dayOffSymbol))
        return self.cursor.fetchall()

    def clearTable(self):
        self.cursor.execute('DROP TABLE IF EXISTS calendar')

    def toString(self):
        self.cursor.execute('SELECT * FROM calendar ORDER BY dayNum')
        aList = []
        for day in self.cursor.fetchall():
            aList.append(day)
        return aList
