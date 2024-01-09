from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.


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