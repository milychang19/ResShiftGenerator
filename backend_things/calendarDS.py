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
        self.calendarDblArr = [[0 for a in range(monthTuple[1])] for b in range(numEmployees)]

    def adjustDayNum(f):
        """
        Before every method w/ an @adjustDayNum, dayNum will be dayNum - 1
        """
        def wrapper(self, dayNum, *args, **kwargs):
            adjusted_day_num = dayNum - 1
            result = f(self, adjusted_day_num, *args, **kwargs)
            return result
        return wrapper
    
    def getEmployeeShift(self, employeeNum):
        return self.calendarDblArr[employeeNum]
    
    def getCalendar(self):
        return self.calendarDblArr
    
    def getStartDay(self):
        return self.getStartDay
    
    def getNumEmployees(self):
        return self.numEmployees
    
    @adjustDayNum
    def getShiftType(self, dayNum, employeeNum):
        """
        Returns an employee's shift type on a specific day

        :param employeeNum: An index representing the employee. (int)
        :param dayNum: Number representing the day. (int)
        :return: A shift type represented by an integer
        :rtype: int
        """
        return self.calendarDblArr[employeeNum][dayNum]

    @adjustDayNum
    def assignEmployeeShift(self, employeeNum, dayNum, shiftTypeNum):
        """
        Assigns a employee a specific type of shift

        :param employeeNum: An index representing the employee. (int)
        :param dayNum: Number representing the day. (int)
        :param shiftTypeNum: Number representing the shift type. (int)
        """
        self.calendarDblArr[employeeNum][dayNum] = shiftTypeNum
    
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
    
    @adjustDayNum
    def unavailableEmployees(self, dayNum, unavailableNum):
        """
        Returns list of employees whom are unavailable for the day

        :param dayNum: Number representing the day.(int)
        :param unavailableNum: The number representing an called off day. (int)
        :return: List of employees whose status matches the unavailableNum
        :rtype: List
        """
        unavailable = []
        for a in range(self.numEmployees):
            if (self.calendarDblArr[a][dayNum] == unavailableNum):
                unavailable.append(a)
        return unavailable




myCalender = calendarDS(5,2023,12)
print(myCalender.getShiftType(12,4))
