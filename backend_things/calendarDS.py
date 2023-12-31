import calendar
class calendarDS:
    def __init__(self, numEmployees, year, month):
        """
        Assigns a employee a specific type of shift

        :param numEmployees: Number of employees we're dealing with. (int)
        :param year: The year in question. (int)
        :param month: The month in question. (int)
        """
        self.numEmployees = int(numEmployees)

        monthTuple = calendar.monthrange(year, month)
        self.startDay = int(monthTuple[0])
        self.calendarDblArr = [["___" for a in range(monthTuple[1])] for b in range(numEmployees)]
        self.numDays = int(monthTuple[1])
    
    def getEmployeeShift(self, employeeNum):
        return self.calendarDblArr[employeeNum]
    
    def getCalendar(self):
        return self.calendarDblArr
    
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
        :return: A shift type represented by an integer
        :rtype: int
        """
        dayNum -= 1
        return self.calendarDblArr[employeeNum][dayNum]

    def assignEmployeeShift(self, employeeNum, dayNum, shiftTypeNum):
        """
        Assigns a employee a specific type of shift

        :param employeeNum: An index representing the employee. (int)
        :param dayNum: Number representing the day. (int)
        :param shiftTypeNum: Number representing the shift type. (int)
        """
        dayNum -= 1
        self.calendarDblArr[employeeNum][dayNum] = shiftTypeNum
    
    def isEmployeeAssigned(self, employeeNum, dayNum):
        dayNum -= 1
        if self.calendarDblArr[employeeNum][dayNum] == "___": return False
        else: return True

    def isShiftTypeFilled(self, dayNum, shiftTypeNum):
        """
        Checks if there are enough people assigned a shift type for a specific day

        :param dayNum: Number representing the day.(int)
        :param shiftTypeNum: The number representing the shift type. (int)
        :return: T/F to see if the shift type quota has been met
        :rtype: bool
        """
        for a in range(self.numEmployees):
            if (self.calendarDblArr[a][dayNum] == shiftTypeNum):
                return True
        return False
    
    def unavailableEmployees(self, dayNum, dayOffSymbol):
        """
        Returns list of employees whom are unavailable for the day

        :param dayNum: Number representing the day.(int)
        :param unavailableNum: The number representing an called off day. (int)
        :return: List of employees whose status matches the unavailableNum
        :rtype: List
        """
        dayNum -= 1
        unavailable = []
        for a in range(self.numEmployees):
            if (self.calendarDblArr[a][dayNum] == dayOffSymbol):
                unavailable.append(a)
        return unavailable

    def toString(self):
        a = 0
        for aStaff in self.calendarDblArr:
            print(f"{a}: ", end="")
            a += 1
            b = 1
            for day in aStaff:
                print(f"({b}) {day}", end=" ")
                b += 1
            print("", end="\n")
                
    def printCalendar(year, month):
        '''
        Print the month
        '''
        print(calendar.month(year,month))