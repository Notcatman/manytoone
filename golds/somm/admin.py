from django.contrib import admin
from .models import Car, LicensePlate, Album, Song, Member, Team

admin.site.register(Car)
admin.site.register(LicensePlate)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Team)
admin.site.register(Member)

