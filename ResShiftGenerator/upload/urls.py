from django.urls import path 
from . import views

#URL CONF
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about_us, name = 'about'),
    path('generator/', views.generator, name = 'generator'),
    path('guide/', views.user_guide, name = 'guide'),
    path('teams/', views.res_team, name = 'teams'),
]