from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
# Create your views here.
"""
import mysql.connector


conection= mysql.connector.connect(user='root', 
host='localhost', port='3306', password='12345678')
myquery=conection.cursor()
myquery.execute("select something from data.table")

for q in myquery:
    results += q
"""

import mysql.connector
cnx = mysql.connector.connect(user='root', 
host='localhost', port='3306', password='1234', database="premier_league")
cursor = cnx.cursor(buffered=True)

def get_all_matches(request):
    cursor.execute("SELECT * FROM match_game")
    players = cursor.fetchall()
    for player in players:
        print(player)

    return HttpResponse("Test Worked")


    