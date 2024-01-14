from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from sqlite3 import Error

from .pandasDF import csvtosql

# Create your views here.

def index(request):
    path = '/Users/richardcui/Desktop/Random Projects/ResShiftGenerator/ResShiftGenerator/shifts/mycsvfile.csv'
    nut = csvtosql(path)
    nut.fillDaysOff()
    nut.runAlgorithm(31)
    what = nut.printCal()
    return render(request, 'shifts/index.html', {
        "nut": what
    })