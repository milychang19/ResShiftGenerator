from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about-us.html')

def generator(request):
    return render(request, 'generator.html')

def res_team(request):
    return render(request, 'res-team.html')

def user_guide(request):
    return render(request, 'user-guide.html')


# Inside csvapp/views.py
def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return render(request, 'upload_csv.html', {'error': 'Please upload a CSV file'})
        
        data = pd.read_csv(csv_file)
        #Convert DF to HTML table
        data_html = data.to_html()
        #Do something with the data (e.g., pass it to a template)
        return render(request, 'display_data.html', {'data_html':data_html})
    
    return render(request, 'upload_csv.html')