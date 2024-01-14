import pandas as pd
import sqlite3
import ast
import sys
import random
from shifts.calendarDS import calendarDS

YEAR = 2024
MONTH = 3

class csvtosql:
    def __init__(self, csvfile):
        try:
            self.dataframe = pd.read_csv(csvfile, index_col="stuID")
        except FileNotFoundError as e:
            sys.exit("No such file")
        self.calendar = calendarDS(YEAR, MONTH)
        self.MAXSHIFTS = 50
    
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

            
    def getTimeOff(self, index):
        try:
            timeOff = ast.literal_eval(self.dataframe["timeOff"][index])
        except Exception as e:
            sys.exit("Error with timeOff")
        return timeOff
    def createPrioList(self, numDays):
        '''
        Creates and sorts a list of days off in descending order based off most requested days

        :param numDays: The number of days in the month of interest

        :rtype: list
        :return: The most requested days off sorted in descending order
        '''
        listOfDaysOff = dict.fromkeys(range(1,numDays+1), 0)
        for index in self.dataframe.index:
            for dayOff in self.getTimeOff(index):
                listOfDaysOff[dayOff] += 1
        listOfDaysOff = sorted(listOfDaysOff.items(), key = lambda x: x[1], reverse=True)
        listOfDaysOff = [tup[0] for tup in listOfDaysOff]
        return listOfDaysOff

    def fillDaysOff(self):
        for index in self.dataframe.index:
            for dayOff in self.getTimeOff(index):
                self.calendar.assignEmployeeShift(index, dayOff, 'off')
    
    def sublistOfStaff(self, shiftType, shiftCount):
        listOfStaffID = []
        try:
            for index in self.dataframe.index:
                if self.dataframe[shiftType][index] == shiftCount:
                    listOfStaffID.append(index)   
        except Exception as e:
            sys.exit("Invalid shift type")        
        return listOfStaffID    
    
    def getShiftCountList(self, shiftType):
        shiftCountList = self.dataframe.loc[:, shiftType].to_list()
        shiftCountList.sort()
        shiftCountList = list(dict.fromkeys(shiftCountList))
        return shiftCountList
    def myCoolHashFunc(self, nut, bound):
        if (bound != 0):
            return nut % bound
        return 0
    def runAlgorithm(self, numDays):
        for day in self.createPrioList(numDays):
            for shiftType in self.getShiftTypes():
                staffAssigned = False
                randNum = random.randint(0,len(self.dataframe))

                for shiftCount in self.getShiftCountList(shiftType):
                    if staffAssigned:
                        break
                    prioStaff = self.sublistOfStaff(shiftType, shiftCount)
                    #print(f"NUM: {shiftCount} SHIFT TYPE: {shiftType} Sublist of staff: {prioStaff}")
                    for a in range(len(prioStaff)):
                        staffID = prioStaff[self.myCoolHashFunc(randNum + a, len(prioStaff))]
                        #print(f"CURRENT stafID: {staffID}")
                        if self.calendar.isEmployeeAssigned(staffID, day) is False and staffID not in self.calendar.unavailableEmployees(day, 'off'):
                            self.calendar.assignEmployeeShift(staffID, day, shiftType)
                            self.dataframe.loc[staffID, shiftType] += 1
                            #print(f"ASSIGNED!!: {staffID}")
                            staffAssigned = True
                            break
                if not staffAssigned:
                    sys.exit(f"Issue with day {day}. Try restarting program or clear schedule conflict")

    def printCal(self):
        return self.calendar.toString()
    def deleteCal(self):
        self.calendar.clearTable()
    def printDF(self):
        print(self.dataframe)
    def getDF(self):
        return self.dataframe