import calendarDS
import csv

#this is staff.csv except in a list of dicts
testData = [
    {"numID": 0, "stuID": 86572, "stuName": "Emily", "timeOff": [13,14,29,3,10], "PH": 3, "NH": 5},
    {"numID": 1, "stuID": 75432, "stuName": "Richard", "timeOff": [13,14,25,19,9], "PH": 4, "NH": 5},
    {"numID": 2, "stuID": 23758, "stuName": "Molin", "timeOff": [14,16,7,9,23], "PH": 3, "NH": 4},
    {"numID": 3, "stuID": 76546, "stuName": "Drake", "timeOff": [13,5,1,7,28], "PH": 5, "NH": 3},
    {"numID": 4, "stuID": 65789, "stuName": "Cardib", "timeOff": [5,17,18,21,27], "PH": 4, "NH": 3}
]

residenceBuildings = [
    "LA", "Gordon", "Martime", "Mountain", "Prairie", "Village", "Towers", 
    "Johnston", "Maids", "Mills", "Watson", "Lambton"
]

fieldnames = ['numID', 'stuID', 'stuName', 'timeOff', 'PH', 'NH']
# Write all members info to file "teamInfo.csv"
with open("teamInfo.csv", mode="w", newline='') as csvFile:
    CSVdict = csv.DictWriter(csvFile, fieldnames=fieldnames)
    CSVdict.writeheader()
    for emp in testData:
        CSVdict.writerow(emp)

with open("residence.csv", mode="w", newline='') as csvFile:
    CSVdict = csv.DictWriter(csvFile, fieldnames = fieldnames)
    CSVdict.writeheader()
    for building in residenceBuildings:
        CSVdict.writerow(building)


MONTH = 12
YEAR = 2023



class algo:# why do we need a algorithm class? I think def would be enough
    def ascendingSort(listOfStaff, shiftType):
        listOfStaff.sort(key=lambda staff: staff[shiftType])
        return listOfStaff
    def subarrayOfShiftType(self, listOfStaff, shiftType):
        listOfStaff = self.ascendingSort(listOfStaff, shiftType)
        ##
    
dataStructure = calendarDS(len(testData), YEAR, MONTH)

    
