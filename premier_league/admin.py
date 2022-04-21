from django.contrib import admin

# Register your models here.

from .models import *

#admin.site.register('club')


admin.site.register(Club)
admin.site.register(MatchGame)
admin.site.register(Player)
admin.site.register(PlayerClubSeason)
admin.site.register(Review)
admin.site.register(Stadium)
admin.site.register(Fan)
