from django.contrib import admin
from .models import Planet, Species, Vehicle, Starship, Character, Movie, UserCharacter, UserPlanet, UserWildlife, Wildlife

# Register your models here.

admin.site.register(Planet)
admin.site.register(Species)
admin.site.register(Vehicle)
admin.site.register(Starship)
admin.site.register(Character)
admin.site.register(Movie)
admin.site.register(Wildlife)
admin.site.register(UserCharacter)
admin.site.register(UserPlanet)
admin.site.register(UserWildlife)
