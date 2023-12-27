import calendarDS
import csv

#this is staff.csv except in a list of dicts
testData = [
    {"numID": 0, "stuID": 86572, "stuName": "emily", "timeOff": [13,14,29,3,10], "PH": 3, "NH": 5},
    {"numID": 1, "stuID": 75432, "stuName": "richard", "timeOff": [13,14,25,19,9], "PH": 4, "NH": 5},
    {"numID": 2, "stuID": 23758, "stuName": "molin", "timeOff": [14,16,7,9,23], "PH": 3, "NH": 4},
    {"numID": 3, "stuID": 76546, "stuName": "drake", "timeOff": [13,5,1,7,28], "PH": 5, "NH": 3},
    {"numID": 4, "stuID": 65789, "stuName": "cardib", "timeOff": [5,17,18,21,27], "PH": 4, "NH": 3}
]

listOfBuildings = [
    "LA", "Gordon", "Martime", "Mountain", "Prairie", "Village", "Towers", 
    "Johnston", "Maids", "Mills", "Watson", "Lambton"
]

fieldnames = ['numID', 'stuID', 'stuName', 'timeOff', 'PH', 'NH']
with open("people.csv", mode="w", newline='') as csvFile:
    CSVdict = csv.DictWriter(csvFile, fieldnames=fieldnames)
    CSVdict.writeheader()
    for emp in testData:
        CSVdict.writerow(emp)


MONTH = 12
YEAR = 2023



class algo:
    def ascendingSort(listOfStaff, shiftType):
        listOfStaff.sort(key=lambda staff: staff[shiftType])
        return listOfStaff
    def subarrayOfShiftType(self, listOfStaff, shiftType):
        listOfStaff = self.ascendingSort(listOfStaff, shiftType)
        ##
    
dataStructure = calendarDS(len(testData), YEAR, MONTH)

    
