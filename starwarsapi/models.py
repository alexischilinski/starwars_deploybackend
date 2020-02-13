from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Planet(models.Model):
    name=models.CharField(max_length=200)
    climate=models.CharField(max_length=200, null=True)
    terrain=models.CharField(max_length=200, null=True)
    image=models.CharField(max_length=200, null=True, blank=True)

class Species(models.Model):
    name=models.CharField(max_length=200)
    classification=models.CharField(max_length=200, null=True)
    language=models.CharField(max_length=200, null=True)

class Vehicle(models.Model):
    name=models.CharField(max_length=200)
    manufacturer=models.CharField(max_length=200, null=True)
    max_speed=models.IntegerField(null=True)
    passengers=models.IntegerField(null=True)    
    vehicle_class=models.CharField(max_length=200, null=True)

class Starship(models.Model):
    name=models.CharField(max_length=200)
    manufacturer=models.CharField(max_length=200, null=True)
    max_speed=models.IntegerField(null=True)
    passengers=models.IntegerField(null=True)    
    starship_class=models.CharField(max_length=200, null=True)

class Movie(models.Model):
    title=models.CharField(max_length=200)
    episode=models.IntegerField()
    roman_numeral=models.CharField(max_length=5, blank=True)
    opening_crawl=models.CharField(max_length=1000, blank=True)
    poster=models.CharField(max_length=1000, blank=True)
    # characters=models.ManyToManyField(Character, through="CharacterMovie")

class Character(models.Model):
    name=models.CharField(max_length=200)  
    gender=models.CharField(max_length=200, null=True)
    planet=models.CharField(max_length=200, null=True)
    species=models.CharField(max_length=200, null=True)    
    image=models.CharField(max_length=200, null=True)
    force_sensitive=models.BooleanField(null=True, blank=True)
    side=models.CharField(max_length=200, null=True, blank=True)
    role=models.CharField(max_length=200, null=True, blank=True)
    quote=models.CharField(max_length=200, null=True, blank=True)
    lightsaber=models.CharField(max_length=200, null=True, blank=True)
    sith_name=models.CharField(max_length=200, null=True, blank=True)
    movies=models.ManyToManyField(Movie, through="CharacterMovie")

class CharacterMovie(models.Model):
    character=models.ForeignKey(Character, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)

class Wildlife(models.Model):
    name=models.CharField(max_length=200)
    classification=models.CharField(max_length=200, null=True, blank=True)
    habitat=models.CharField(max_length=200, null=True, blank=True)
    diet=models.CharField(max_length=200, null=True, blank=True)
    image=models.CharField(max_length=200, null=True, blank=True)

class UserCharacter(models.Model):
    user=models.ForeignKey(User, related_name="usercharacters", on_delete=models.CASCADE, null=True)
    category=models.CharField(max_length=200, default='character')
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200, null=True, blank=True)
    planet=models.CharField(max_length=200, null=True, blank=True)
    species=models.CharField(max_length=200, null=True, blank=True)    
    image=models.CharField(max_length=500, null=True, blank=True)
    force_sensitive=models.BooleanField(null=True, blank=True)
    side=models.CharField(max_length=200, null=True, blank=True)
    role=models.CharField(max_length=200, null=True, blank=True)
    best_quote=models.CharField(max_length=200, null=True, blank=True)
    lightsaber=models.CharField(max_length=200, null=True, blank=True)
    sith_name=models.CharField(max_length=200, null=True, blank=True)

class UserPlanet(models.Model):
    user=models.ForeignKey(User, related_name="userplanets", on_delete=models.CASCADE, null=True)
    category=models.CharField(max_length=200, default='planet')
    name=models.CharField(max_length=200)
    climate=models.CharField(max_length=200, null=True, blank=True)
    terrain=models.CharField(max_length=200, null=True, blank=True)
    image=models.CharField(max_length=500, null=True, blank=True)

class UserWildlife(models.Model):
    user=models.ForeignKey(User, related_name="userwildlife", on_delete=models.CASCADE, null=True)
    category=models.CharField(max_length=200, default='animal')
    name=models.CharField(max_length=200)
    classification=models.CharField(max_length=200, null=True, blank=True)
    habitat=models.CharField(max_length=200, null=True, blank=True)
    diet=models.CharField(max_length=200, null=True, blank=True)
    image=models.CharField(max_length=500, null=True, blank=True)


