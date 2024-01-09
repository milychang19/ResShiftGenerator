from django.urls import path 
from . import views

#URL CONF
urlpatterns = [
    path ('csv/', views.upload_csv)
]