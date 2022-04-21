from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
 
from .models import *
 
urlpatterns = [
    path('get_all_matches/', views.get_all_matches, name="get_all_matches"),
]

