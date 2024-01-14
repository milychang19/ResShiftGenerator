from database.calendarDS import calendarDS, staffDS
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
listOfShiftTypes = ['ph1', 'nh1', 'ph2', 'nh2', 'backup']

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
                        print(f"Issue with {dayNum}. Will need external help")
                        sys.exit()
    ds.toString()
    for staff in testData:
        print(staff)
    
main()







    
