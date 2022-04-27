from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
 
from .models import *
 
urlpatterns = [
    path('get_all_matches/', views.get_all_matches, name="get_all_matches"),
    path('insert_match_review/', views.insert_match_review, name="insert_match_review"),
    path('show_match_review/', views.show_match_review, name="show_match_review"),
    path('insert_fan/', views.insert_fan, name="insert_fan"),



]

