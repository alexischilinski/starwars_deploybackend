from rest_framework import serializers
from starwarsapi.models import Planet, Species, Character, Vehicle, Starship, Movie, CharacterMovie, Wildlife, UserPlanet, UserWildlife, UserCharacter

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ('id', 'name', 'climate', 'terrain', 'image')

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('id', 'name', 'classification', 'language')

class CharacterMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterMovie
        fields = ('id', 'character', 'movie')
        depth = 3

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'name', 'gender', 'species', 'planet', 'image', 'force_sensitive', 'side', 'role', 'lightsaber', 'quote', 'sith_name', 'movies')
        depth = 1

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'episode', 'roman_numeral', 'opening_crawl', 'poster')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('__all__')

class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = ('__all__')

class WildlifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wildlife
        fields = ('__all__')

class UserCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCharacter
        fields = ('__all__')

class UserPlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlanet
        fields = ('__all__')

class UserWildlifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWildlife
        fields = ('__all__')