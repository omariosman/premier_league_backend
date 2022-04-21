# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Club(models.Model):
    club_name = models.CharField(primary_key=True, max_length=100)
    stadium_name = models.ForeignKey('Stadium', models.DO_NOTHING, db_column='stadium_name', blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fan(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    favorite_team = models.ForeignKey(Club, models.DO_NOTHING, db_column='favorite_team', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fan'


class MatchGame(models.Model):
    home_team_red_cards = models.CharField(max_length=100, blank=True, null=True)
    away_team_red_cards = models.CharField(max_length=45, blank=True, null=True)
    goals_home = models.CharField(max_length=45, blank=True, null=True)
    goals_away = models.CharField(max_length=45, blank=True, null=True)
    season = models.CharField(max_length=45, blank=True, null=True)
    match_date = models.CharField(primary_key=True, max_length=45)
    home_team_possession = models.CharField(max_length=45, blank=True, null=True)
    away_team_possession = models.CharField(max_length=45, blank=True, null=True)
    home_team_shots = models.CharField(max_length=45, blank=True, null=True)
    away_team_shots = models.CharField(max_length=45, blank=True, null=True)
    home_team_yellow_cards = models.CharField(max_length=45, blank=True, null=True)
    away_team_yellow_cards = models.CharField(max_length=45, blank=True, null=True)
    home_team_fouls = models.CharField(max_length=45, blank=True, null=True)
    away_team_fouls = models.CharField(max_length=45, blank=True, null=True)
    home_team = models.CharField(max_length=45)
    away_team = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'match_game'
        unique_together = (('match_date', 'home_team', 'away_team'),)


class Player(models.Model):
    player_name = models.CharField(primary_key=True, max_length=50, db_collation='utf8mb4_0900_ai_ci')
    player_position = models.CharField(max_length=50, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    height = models.CharField(max_length=50, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    nationality = models.CharField(max_length=50, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    date_of_birth = models.CharField(max_length=50, db_collation='utf8mb4_0900_ai_ci')
    weight = models.CharField(max_length=20, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'
        unique_together = (('player_name', 'date_of_birth'),)


class PlayerClubSeason(models.Model):
    player_name = models.OneToOneField(Player, models.DO_NOTHING, db_column='player_name', primary_key=True)
    date_of_birth = models.ForeignKey(Player, models.DO_NOTHING, related_name = 'playerDOB', db_column='date_of_birth')
    club_name = models.ForeignKey(Club, models.DO_NOTHING, db_column='club_name')
    season = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'player_club_season'
        unique_together = (('player_name', 'date_of_birth', 'club_name', 'season'),)


class Review(models.Model):
    fan_username = models.OneToOneField(Fan, models.DO_NOTHING, db_column='fan_username', primary_key=True)
    rating = models.IntegerField(blank=True, null=True)
    review_text = models.CharField(max_length=255, blank=True, null=True)
    match_date = models.CharField(max_length=45)
    home_team = models.ForeignKey(Club, models.DO_NOTHING, db_column='home_team')
    away_team = models.ForeignKey(Club, models.DO_NOTHING, related_name = 'reviewAwayTeam', db_column='away_team')

    class Meta:
        managed = False
        db_table = 'review'
        unique_together = (('fan_username', 'match_date', 'home_team', 'away_team'),)


class Stadium(models.Model):
    stadium_name = models.CharField(primary_key=True, max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.CharField(max_length=100, blank=True, null=True)
    record_league_attendance = models.CharField(max_length=100, blank=True, null=True)
    building_date = models.CharField(max_length=100, blank=True, null=True)
    pitch_size = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stadium'
