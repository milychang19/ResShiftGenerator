from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Staff

# Create your views here.
def index(request):
    return render(request, 'shifts/index.html', {
        'nut': Staff.objects.all()
    })