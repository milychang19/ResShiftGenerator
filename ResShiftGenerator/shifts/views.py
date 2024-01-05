from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import sqlite3
from sqlite3 import Error

from .models import Staff, Calendar

# Create your views here.

testData = [
    {"numID": 0, "stuID": 86572, "stuName": "Emily", "timeOff": [13,14,29,3,10], "PH1": 3, "NH2": 5},
    {"numID": 1, "stuID": 75432, "stuName": "Richard", "timeOff": [13,14,25,19,9], "PH1": 4, "NH2": 5},
    {"numID": 2, "stuID": 23758, "stuName": "Molin", "timeOff": [14,16,7,9,23], "PH1": 5, "NH2": 4},
    {"numID": 3, "stuID": 76546, "stuName": "Drake", "timeOff": [13,5,1,7,28], "PH1": 5, "NH2": 3},
    {"numID": 4, "stuID": 65789, "stuName": "Cardib", "timeOff": [5,17,18,21,27], "PH1": 3, "NH2": 3}
]
listOfShiftTypes = ["PH1", "NH2"]

def index(request):
    return render(request, 'shifts/index.html', {
        'nut': Staff.objects.all(),
        'but': Calendar.objects.all()
    })