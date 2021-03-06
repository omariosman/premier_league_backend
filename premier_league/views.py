import email
from django.forms import GenericIPAddressField
from django.shortcuts import render
from django.http import HttpResponse
from sqlalchemy import JSON
from .models import * 
import json
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from decimal import Decimal
# Create your views here.

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)



import mysql.connector
cnx = mysql.connector.connect(user='admin', 
host='database-1.c5knnxynfhmf.ca-central-1.rds.amazonaws.com', port='3306', password='osman123', database="premier_league")
cursor = cnx.cursor(buffered=True)



def get_all_matches(request):
    cursor.execute("SELECT * FROM match_game")
    matches = cursor.fetchall()
    return HttpResponse(json.dumps(matches, cls=DecimalEncoder), content_type="application/json")


def insert_match_review(request):
    data = JSONParser().parse(request)
    print("data: ", data)
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


    

def get_nationality(request):
    cursor.execute("SELECT distinct nationality FROM player")
    nationality = cursor.fetchall()
    print(nationality)
    return HttpResponse(json.dumps(nationality), content_type="application/json")

def get_players_with_nationality(request):
    data = JSONParser().parse(request)
    nationality = data["nationality"]
    nationality = data["nationality"]
    query = """SELECT p.player_name, p.date_of_birth, p.nationality, pc.season, pc.club_name FROM premier_league.player as p join player_club_season_main as pc on pc.player_name = p.player_name and pc.date_of_birth = p.date_of_birth where nationality=%s;"""
    tuple1 = (nationality,)
    cursor.execute(query, tuple1)
    players_with_nationality = cursor.fetchall()
    return HttpResponse(json.dumps(players_with_nationality), content_type="application/json")


def get_positions(request):
    cursor.execute("SELECT distinct player_position FROM player")
    positions = cursor.fetchall()
    print(positions)
    return HttpResponse(json.dumps(positions), content_type="application/json")

def get_players_with_position(request):
    data = JSONParser().parse(request)
    pos = data["position"]
    query = """SELECT * from player where player_position=%s;"""
    tuple1 = (pos,)
    cursor.execute(query, tuple1)
    players_with_position = cursor.fetchall()
    return HttpResponse(json.dumps(players_with_position), content_type="application/json")




def get_clubs(request):
    cursor.execute("SELECT distinct club_name FROM club")
    clubs = cursor.fetchall()
    print(clubs)
    return HttpResponse(json.dumps(clubs), content_type="application/json")


def get_club_info(request):
    data = JSONParser().parse(request)
    club_name = data["club_name"]
    query = """SELECT * FROM club c where c.club_name=%s;"""
    tuple1 = (club_name,)
    cursor.execute(query, tuple1)
    club_info = cursor.fetchall()
    return HttpResponse(json.dumps(club_info), content_type="application/json")




def get_players(request):
    cursor.execute("SELECT distinct player_name FROM player")
    players = cursor.fetchall()
    print(players)
    return HttpResponse(json.dumps(players), content_type="application/json")


def get_player_info(request):
    data = JSONParser().parse(request)
    player_name = data["player_name"]
    query = """SELECT * FROM player p where p.player_name=%s;"""
    tuple1 = (player_name,)
    cursor.execute(query, tuple1)
    player_info = cursor.fetchall()
    return HttpResponse(json.dumps(player_info), content_type="application/json")




def get_stadiums(request):
    cursor.execute("SELECT distinct stadium_name FROM stadium")
    stadiums = cursor.fetchall()
    print(stadiums)
    return HttpResponse(json.dumps(stadiums), content_type="application/json")



def get_stadium_info(request):
    data = JSONParser().parse(request)
    stadium_name = data["stadium_name"]
    query = """select c.club_name, s.stadium_name from club c join stadium s on s.stadium_name = c.stadium_name where s.stadium_name =%s;"""
    tuple1 = (stadium_name,)
    cursor.execute(query, tuple1)
    stadium_info = cursor.fetchall()
    return HttpResponse(json.dumps(stadium_info), content_type="application/json")


def get_top_teams_by_matches_won(request):
    cursor.execute("""
    select home_team as team, count(*) as count from match_game where goals_home > goals_away
    union
    select away_team as team, count(*) as count from match_game where goals_home < goals_away
    group by team  
    order by count, team DESC limit 10
    """)
    top_teams = cursor.fetchall()
    return HttpResponse(json.dumps(top_teams), content_type="application/json")



def get_top_teams_by_home_matches_won(request):
    cursor.execute("""
    select home_team as team, count(*) as count from match_game where goals_home > goals_away
    group by home_team
    order by count 
    DESC limit 10;
    """)
    top_teams = cursor.fetchall()
    return HttpResponse(json.dumps(top_teams), content_type="application/json")


def get_top_teams_by_yellow_cards(request):
    cursor.execute("""
    select home_team as team, sum(home_team_yellow_cards) as cards_count from match_game
    group by home_team
    union
    select away_team as team, sum(away_team_yellow_cards) as cards_count from match_game
    group by away_team
    order by cards_count
    desc limit 10;
    """)
    top_teams = cursor.fetchall()
    return HttpResponse(json.dumps(top_teams, cls=DecimalEncoder), content_type="application/json")

def get_top_teams_by_shots(request):
    cursor.execute("""
    select home_team as team, sum(home_team_shots) as shots_count from match_game
    group by home_team
    union
    select away_team as team, sum(away_team_shots) as fouls_count from match_game
    group by away_team
    order by shots_count
    desc limit 10;
    """)
    top_teams = cursor.fetchall()
    return HttpResponse(json.dumps(top_teams, cls=DecimalEncoder), content_type="application/json")




def get_top_teams_by_fouls(request):
    cursor.execute("""
    select home_team as team, sum(home_team_fouls) as fouls_count from match_game
    group by home_team
    union
    select away_team as team, sum(away_team_fouls) as fouls_count from match_game
    group by away_team
    order by fouls_count
    desc limit 10;
    """)
    top_teams = cursor.fetchall()
    return HttpResponse(json.dumps(top_teams,  cls=DecimalEncoder), content_type="application/json")


def get_top_teams_by_season(request):
    cursor.execute("""
    select season, team , max(count) from
    (
    select season, home_team as team, count(*) as count from match_game where goals_home > goals_away
    union
    select season, away_team as team, count(*) as count from match_game where goals_home < goals_away
    group by season, team
    ) tb
    group by season;
    """)
    top_teams = cursor.fetchall()
    return HttpResponse(json.dumps(top_teams,  cls=DecimalEncoder), content_type="application/json")


def all_users(request):
    cursor.execute("SELECT distinct username FROM fan")
    all_users = cursor.fetchall()
    #print(all_users)
    return HttpResponse(json.dumps(all_users), content_type="application/json")



"""
top 10 teams by yellow cards
select home_team as team, sum(home_team_yellow_cards) as cards_count from match_game
group by home_team
union
select away_team as team, sum(away_team_yellow_cards) as cards_count from match_game
group by away_team
order by cards_count
desc limit 10;

top 10 teams by fouls
select home_team as team, sum(home_team_fouls) as fouls_count from match_game
group by home_team
union
select away_team as team, sum(away_team_fouls) as fouls_count from match_game
group by away_team
order by fouls_count
desc limit 10;

top 10 teams by shots
select home_team as team, sum(home_team_shots) as shots_count from match_game
group by home_team
union
select away_team as team, sum(away_team_shots) as fouls_count from match_game
group by away_team
order by shots_count
desc limit 10;

top 10 teams by matches_won
select home_team as team, count(*) as count from match_game where goals_home > goals_away
union
select away_team as team, count(*) as count from match_game where goals_home < goals_away
group by team
order by count DESC limit 10

top 10 teams by home_matches_won
select home_team as team, count(*) as count from match_game where goals_home > goals_away
group by home_team
order by count 
DESC limit 10;

show all the teams who won the most games by season
select season, team , max(count) from
(
select season, home_team as team, count(*) as count from match_game where goals_home > goals_away
union
select season, away_team as team, count(*) as count from match_game where goals_home < goals_away
group by season, team
) tb
group by season;
"""
