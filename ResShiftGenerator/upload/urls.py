from django.urls import path 
from . import views

#URL CONF
urlpatterns = [
    path ('', views.home),
    path('about/', views.about_us),
    path('generator/', views.generator),
    path('teams/', views.res_team),
    path ('csv/', views.upload_csv)
]