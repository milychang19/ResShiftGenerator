from calendarDS import calendarDS
import random
import sys

MONTH = 12
YEAR = 2023
NUMPAIRS = 1
MAXNUMDAYS = 31
LIMITONSHIFTS = 200

#this is staff.csv except in a list of dicts
#fyi try not to delete files until the end bc we need them for version control
testData = testData = [
    {"numID": i,
     "stuID": random.randint(10000, 99999),
     "stuName": "Name" + str(i),
     "timeOff": random.sample(range(1, 32), 5),
     "PH1": random.randint(3, 5),
     "NH1": random.randint(3, 5),
     "PH2": random.randint(3, 5),
     "NH2": random.randint(3, 5),
     "BCK": random.randint(3, 5)
    }
    for i in range(20)
]

#gotta figure out how to dynamically change this depending on team and stuff
listOfShiftTypes = ["PH1", "NH1", "PH2", "NH2", "BCK"]

def fillDaysOffCalendar(listOfStaff, calendar):
    '''
    Fills data structure with days off

    :param listOfStaff: It's the list of dicts that holds info of all the peeps (staff)
    :param calendar: The data structure
    '''
    for staff in listOfStaff:
        for dayOff in staff["timeOff"]:
            calendar.assignEmployeeShift(staff["numID"], dayOff, "OFF")


def findMinShiftCount(listOfStaff, shiftType):
    '''
    Finds the minimum assigned shift type based off of shift type

    :param listOfStaff: It's the list of dicts that holds info of all the peeps (staff)
    :param shiftType: The shift type (like 1st pack holder)

    :rtype: int
    :return: magnitude of minimum assigned shift type
    '''
    minShiftNum = listOfStaff[0][shiftType]
    for staff in listOfStaff:
        if staff[shiftType] < minShiftNum:
            minShiftNum = staff[shiftType]
        
    return minShiftNum

def subarrayOfShiftType(listOfStaff, shiftType, shiftCount):
    '''
    Creates a subarray of staff based off of shift type and shift count

    :param listOfStaff: It's the list of dicts that holds info of all the peeps (staff)
    :param shiftType: The shift type (like 1st pack holder)
    :param shiftCount: Number of shifts worked/assigned for a specific shift type
    '''
    subarrayOfStaff = []
    for staff in listOfStaff:
        if staff[shiftType] == shiftCount:
            subarrayOfStaff.append(staff)
    return subarrayOfStaff


def fillDaysOffList(listOfStaff, numDays):
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
    return listOfDaysOff

def myCoolHashFunc(index, bound):
    if (bound != 0):
        return index % bound
    return 0


def main():
    ds = calendarDS(len(testData), YEAR, MONTH) 

    fillDaysOffCalendar(testData,ds)

    sortedDaysOff = fillDaysOffList(testData, ds.getNumDays())

    for a in sortedDaysOff:
        dayNum = a[0]

        for shiftType in listOfShiftTypes:
            minShiftCount = findMinShiftCount(testData, shiftType)
            staffAssigned = False
            oopsiePoopsieCounter = 0
            randStartPoint = random.randint(0,len(testData))

            while staffAssigned is False:
                subarrayOfStaff = subarrayOfShiftType(testData, shiftType, minShiftCount)
                indexOfStaff = subarrayOfStaff[myCoolHashFunc(randStartPoint + oopsiePoopsieCounter, len(subarrayOfStaff))]["numID"]
                print(f"Index: {indexOfStaff}")

                if indexOfStaff not in ds.unavailableEmployees(dayNum,"OFF") and ds.isEmployeeAssigned(indexOfStaff,dayNum) is False:
                    print(f"Index Assigned: {indexOfStaff}",end="\n\n")
                    ds.assignEmployeeShift(indexOfStaff,dayNum,shiftType)
                    testData[indexOfStaff][shiftType] += 1
                    staffAssigned = True
                else:
                    print("entered else", end="\n\n")
                    oopsiePoopsieCounter += 1
                    if oopsiePoopsieCounter >= len(subarrayOfStaff):
                        minShiftCount += 1
                        oopsiePoopsieCounter = 0
                    if minShiftCount == LIMITONSHIFTS:
                        ds.toString()
                        print(f"Issue with {dayNum}th. Will need external help")
                        sys.exit()
    ds.toString()
    for staff in testData:
        print(staff)
    
main()







    
