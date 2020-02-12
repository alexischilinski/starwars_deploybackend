import os 
import requests
from django.core.management.base import BaseCommand
from ...models import Planet, Species, Character, Vehicle, Starship, Movie, CharacterMovie, Wildlife


def get_planets():
    url = 'http://localhost:8000/api/planets/?format=json'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    planets = r.json()
    return planets

def get_species():
    url = 'http://localhost:8000/api/species/?format=json'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    species = r.json()
    return species

def get_characters():
    url = 'http://localhost:8000/api/characters/?format=json'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    characters = r.json()
    return characters

def get_vehicles():
    url = 'http://localhost:8000/api/vehicles/?format=json'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    vehicles = r.json()
    return vehicles

def get_starships():
    url = 'http://localhost:8000/api/starships/?format=json'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    starships = r.json()
    return starships

def get_movies():
    url = 'http://localhost:8000/api/movies/?format=json'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    movies = r.json()
    return movies

def get_animals():
    url = 'http://localhost:8000/api/wildlife/?format=json'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    animals = r.json()
    return animals

def seed_planets():
    for i in get_planets():
        planets = Planet(
            name=i["name"],
            climate=i["climate"],
            terrain=i["terrain"],
            image=i["image"]
        )
        planets.save()

def seed_species():
    for i in get_species():
        species = Species(
            name=i["name"],
            classification=i["classification"],
            language=i["language"]
        )
        species.save()

def seed_characters():
    for i in get_characters():
        characters = Character(
            name=i["name"],
            gender=i["gender"],
            planet=i["planet"],
            species=i["species"],
            image=i["image"],
            force_sensitive=i["force_sensitive"],
            side=i["side"],
            role=i["role"],
            lightsaber=i["lightsaber"],
            quote=i["quote"],
            sith_name=i["sith_name"]
        )
        characters.save()

def seed_vehicles():
    for i in get_vehicles():
        vehicles = Vehicle(
            name=i["name"],
            manufacturer=i["manufacturer"],
            max_speed=i["max_speed"],
            passengers=i["passengers"],
            vehicle_class=i["vehicle_class"]
        )
        vehicles.save()

def seed_starships():
    for i in get_starships():
        starships = Starship(
            name=i["name"],
            manufacturer=i["manufacturer"],
            max_speed=i["max_speed"],
            passengers=i["passengers"],
            starship_class=i["starship_class"]
        )
        starships.save()

def seed_movies():
    for i in get_movies():
        movies = Movie(
            title=i["title"],
            episode=i["episode"],
            opening_crawl=i["opening_crawl"],
            poster=i["poster"]
        )
        movies.save()

def seed_charactersmovies():
    for i in get_characters():
        for movie in i["movies"]:
            for movieObject in Movie.objects.all():
                if (movieObject.title == movie["title"]):
                    for characterObject in Character.objects.all():
                        if (i["name"] == characterObject.name):
                            # import pdb; pdb.set_trace()
                            moviecharacter = CharacterMovie(
                                character=characterObject,
                                movie=movieObject
                            )
                            moviecharacter.save()

def seed_animals():
    for i in get_animals():
        animal = Wildlife(
            name=i["name"],
            classification=i["classification"],
            habitat=i["habitat"],
            diet=i["diet"],
            image=i["image"]
        )
        animal.save()

def clear_data():
    """Deletes all the table data"""
    # Planet.objects.all().delete()
    # Species.objects.all().delete()
    # CharacterMovie.objects.all().delete()
    # Movie.objects.all().delete()
    # Character.objects.all().delete()
    # Vehicle.objects.all().delete()
    # Starship.objects.all().delete()
    # Wildlife.objects.all().delete()

class Command(BaseCommand):
    def handle(self, *args, **options):
        # clear_data()
        # seed_planets()
        # seed_species()
        # seed_movies()
        # seed_characters()
        # seed_vehicles()
        # seed_starships()
        # seed_charactersmovies()
        # seed_animals()
        print("completed")