import pandas as pd
import sqlite3
import ast
import sys
from calendarDS import calendarDS

YEAR = 2024
MONTH = 2

class csvtosql:
    def __init__(self, csvfile):
        self.dataframe = pd.read_csv(csvfile)
        self.calendar = calendarDS(YEAR, MONTH)
    
    def getShiftTypes(self):
        '''
        Returns a list of shift types. Since shift types will always be to the right of 'timeOff',
        if we find the index of 'timeOff', we could slice the list to only hold the shiftTypes
        '''
        listOfShiftTypes = []
        listOfColumns = self.dataframe.columns.tolist()
        if 'timeOff' in listOfColumns:
            timeOffIndex = listOfColumns.index('timeOff')
            listOfShiftTypes = listOfColumns[timeOffIndex+1:]
        return listOfShiftTypes

            
    def getStaffInfo(self, index):
        return self.dataframe.loc[index]
    def createPrioList(self, numDays):
        '''
        Creates and sorts a list of days off in descending order based off most requested days

        :param numDays: The number of days in the month of interest

        :rtype: list
        :return: The most requested days off sorted in descending order
        '''
        listOfDaysOff = dict.fromkeys(range(1,numDays+1), 0)
        for staffIndex in range(len(self.dataframe)):
            staff = self.getStaffInfo(staffIndex)
            try:
                timeOff = ast.literal_eval(staff.timeOff)
            except Exception as e:
                sys.exit("Error with timeOff")

            for dayOff in timeOff:
                listOfDaysOff[dayOff] += 1
        listOfDaysOff = sorted(listOfDaysOff.items(), key = lambda x: x[1], reverse=True)
        listOfDaysOff = [tup[0] for tup in listOfDaysOff]
        return listOfDaysOff

    def fillDaysOff(self):
        for staffIndex in range(len(self.dataframe)):
            staff = self.getStaffInfo(staffIndex)
            try:
                timeOff = ast.literal_eval(staff.timeOff)
            except Exception as e:
                sys.exit("Error with timeOff")
            for dayOff in timeOff:
                self.calendar.assignEmployeeShift(int(staff.stuID), dayOff, 'off')
                
    def printCal(self):
        self.calendar.toString()
    def deleteCal(self):
        self.calendar.clearTable()
    def printDF(self):
        print(self.dataframe)
    
nut = csvtosql('mycsvfile.csv')
nut.fillDaysOff()