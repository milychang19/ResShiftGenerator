from calendarDS import calendarDS
import csv
import pandas as pd
import math
import random

MONTH = 12
YEAR = 2023
NUMPAIRS = 1
MAXNUMDAYS = 31

#this is staff.csv except in a list of dicts
#fyi try not to delete files until the end bc we need them for version control
testData = [
    {"numID": 0, "stuID": 86572, "stuName": "Emily", "timeOff": [13,14,29,3,10], "PH1": 3, "NH2": 5},
    {"numID": 1, "stuID": 75432, "stuName": "Richard", "timeOff": [13,14,25,19,9], "PH1": 4, "NH2": 5},
    {"numID": 2, "stuID": 23758, "stuName": "Molin", "timeOff": [14,16,7,9,23], "PH1": 3, "NH2": 4},
    {"numID": 3, "stuID": 76546, "stuName": "Drake", "timeOff": [13,5,1,7,28], "PH1": 5, "NH2": 3},
    {"numID": 4, "stuID": 65789, "stuName": "Cardib", "timeOff": [5,17,18,21,27], "PH1": 4, "NH2": 3}
]

#gotta figure out how to dynamically change this depending on team and stuff
listOfShiftTypes = ["PH1", "NH1"]

staff_df = pd.DataFrame(testData)


#avg_ph = math.floor(staff_df.groupby('PH').mean())
#num = staff_df[staff_df['PH'] > avg_ph]

#LAWA and JAM are the same team, unless we're tryna do something else here??
residenceBuildings = [
    "Gordon", "Martime", "Mountain", "Prairie", "Village", "Towers", 
    "Johnston", "Maids", "Mills", "Watson", "Lambton", "LA"
]

#fieldnames = ['numID', 'stuID', 'stuName', 'timeOff', 'PH', 'NH']
# Write all members info to file "teamInfo.csv"

""""
with open("teamInfo.csv", mode="w", newline='') as csvFile:
    CSVdict = csv.DictWriter(csvFile, fieldnames= fieldnames)
    CSVdict.writeheader()
    for emp in staff_df:
        CSVdict.writerow(emp)
"""
"""
with open("residence.csv", mode="w", newline='') as csvFile:
    CSVdict = csv.DictWriter(csvFile, fieldnames = fieldnames)
    CSVdict.writeheader()
    for building in residenceBuildings:
        CSVdict.writerow(building)
"""



def findMinShift(listOfStaff, shiftType):
    '''
    A general sorter that sorts the listOfStaff based off of requested shift type

    :param listOfStaff: It's the list of dicts that holds info of all the peeps (staff)
    :param shiftType: The shift type (like 1st pack holder)

    :rtype: list of dicts
    :return: listOfStaff but sorted in ascending order based off of shift type already assigned
    '''
    df = pd.DataFrame(listOfStaff)

    minShiftNum = df[shiftType].min()
    staff_with_min_shift = df[df[shiftType] == minShiftNum].to_dict('lowest')
    return staff_with_min_shift
'''
    listOfStaff[0][shiftType]
    for staff in listOfStaff:
        if staff[shiftType] < minShiftNum:
            minShiftNum = staff[shiftType]
        
    return minShiftNum
'''
    
# what is this ??
def subarrayOfShiftType(listOfStaff, shiftType, minShiftCount):
    subarrayOfStaff = []
    for staff in listOfStaff:
        if staff[shiftType] == minShiftCount:
            subarrayOfStaff.append(staff)
    print(subarrayOfStaff)
    return subarrayOfStaff


def fillDaysOff(listOfStaff, numDays):
    '''
    ***.items() makes the key-value pairs in a dict into a tuple
    ***entry in the lambda function is just the keyvalue pair (or the tuple since we used .items())

    This creates and sorts a list of pairs of days off in descending order based off most requested days

    :param listOfStaff: It's the list of dicts that holds info of all the peeps (staff)
    :param numDays: The number of days in the month of interest

    :rtype: list of pairs
    :return: The most requested days off sorted in descending order
    '''
    listOfDaysOff = {}
    for a in range(numDays):
        listOfDaysOff[a+1] = 0
        for staff in listOfStaff:
            if a+1 in staff["timeOff"]: listOfDaysOff[a+1] += 1
    listOfDaysOff = sorted(listOfDaysOff.items(), key=lambda entry: entry[1], reverse=True)
    print(f"DAY NUM: {numDays}")
    print(listOfDaysOff)
    return listOfDaysOff

def myCoolHashFunc(index, bound):
    if (bound != 0):
        return index % bound
    return 0


def main():
    ds = calendarDS(len(testData), YEAR, MONTH) 

    sortedDaysOff = fillDaysOff(testData, ds.getNumDays())

    for a in sortedDaysOff:
        dayNum = a[0]

        for shiftType in listOfShiftTypes:
            minShiftCount = findMinShift(testData, shiftType)
            staffAssigned = False
            oopsiePoopsieCounter = 0
            randStartPoint = random.randint(0,len(testData))

            while staffAssigned is False:
                subarrayOfStaff = subarrayOfShiftType(testData, shiftType, minShiftCount)
                indexOfStaff = subarrayOfStaff[myCoolHashFunc(randStartPoint + oopsiePoopsieCounter, len(subarrayOfStaff))]["numID"]

                if indexOfStaff not in ds.unavailableEmployees(dayNum,0) and ds.isEmployeeAssigned(indexOfStaff,dayNum) is False:
                    ds.assignEmployeeShift(indexOfStaff,dayNum,shiftType)
                else:
                    oopsiePoopsieCounter += 1
                    if oopsiePoopsieCounter >= len(subarrayOfStaff):
                        minShiftCount += 1
                        oopsiePoopsieCounter = 0
    



main()




    
