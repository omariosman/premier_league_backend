from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
 
from .models import *
 
urlpatterns = [
    path('get_all_matches/', views.get_all_matches, name="get_all_matches"),
    path('insert_match_review/', views.insert_match_review, name="insert_match_review"),
    path('show_match_review/', views.show_match_review, name="show_match_review"),
    path('insert_fan/', views.insert_fan, name="insert_fan"),
    path('get_nationality/', views.get_nationality, name="get_nationality"),
    path('get_players_with_nationality/', views.get_players_with_nationality, name="get_players_with_nationality"),
    path('get_clubs/', views.get_clubs, name="get_clubs"),
    path('get_club_info/', views.get_club_info, name="get_club_info"),
    path('get_players/', views.get_players, name="get_players"),
    path('get_player_info/', views.get_player_info, name="get_player_info"),
    path('get_stadiums/', views.get_stadiums, name="get_stadiums"),
    path('get_stadium_info/', views.get_stadium_info, name="get_stadium_info"),







]

