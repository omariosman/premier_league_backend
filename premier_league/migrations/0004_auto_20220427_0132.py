# Generated by Django 3.2.7 on 2022-04-26 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premier_league', '0003_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_club_d'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Fan',
        ),
        migrations.DeleteModel(
            name='MatchGame',
        ),
        migrations.RemoveField(
            model_name='playerclubseason',
            name='player_name',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Stadium',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='PlayerClubSeason',
        ),
    ]
