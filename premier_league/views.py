import email
from django.forms import GenericIPAddressField
from django.shortcuts import render
from django.http import HttpResponse
from sqlalchemy import JSON
from .models import * 
import json
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
# Create your views here.


import mysql.connector
cnx = mysql.connector.connect(user='root', 
host='localhost', port='3306', password='1234', database="premier_league")
cursor = cnx.cursor(buffered=True)



def get_all_matches(request):
    cursor.execute("SELECT * FROM match_game")
    matches = cursor.fetchall()
    return HttpResponse(json.dumps(matches), content_type="application/json")


def insert_match_review(request):
    data = JSONParser().parse(request)
    username = data["username"]
    rating = data["rating"]
    review_text = data["review"]
    match_date = data["match_date"]
    home_team = data["home_team"]
    away_team = data["away_team"]
    cursor.execute("INSERT INTO review VALUES(%s, %s, %s, %s, %s, %s)", (username, rating, review_text, match_date, home_team, away_team))
    cnx.commit()
    #matches = cursor.fetchall()
    empty_dict = {}
    return HttpResponse(json.dumps(empty_dict), content_type="application/json")



def show_match_review(request):
    data = JSONParser().parse(request)
    print("data: ", data)
    match_date = data["match_date"]
    home_team = data["home_team"]
    away_team = data["away_team"]
    #cursor.execute("SELECT * FROM review WHERE match_date=%s and home_team=? and away_team=?", (match_date, home_team, away_team))
    query = """SELECT * FROM review WHERE match_date=%s and home_team=%s and away_team=%s"""
    tuple1 = (match_date, home_team, away_team)
    cursor.execute(query, tuple1)
    matche_reviews = cursor.fetchall()
    return HttpResponse(json.dumps(matche_reviews), content_type="application/json")



def insert_fan(request):
    data = JSONParser().parse(request)
    username = data["username"]
    email = data["email"]
    gender = data["gender"]
    birthdate = data["birthdate"]
    favorite_team = data["favorite_team"]    
    query = """INSERT INTO fan VALUES(%s, %s, %s, %s, %s)"""
    tuple1 = (username, email, gender, birthdate, favorite_team)
    cursor.execute(query, tuple1)
    cnx.commit()
    #matches = cursor.fetchall()
    empty_dict = {}
    return HttpResponse(json.dumps(empty_dict), content_type="application/json")


    