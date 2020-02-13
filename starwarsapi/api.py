from starwarsapi.models import Planet, Species, Character, Vehicle, Starship, Movie, CharacterMovie, Wildlife, UserPlanet, UserWildlife, UserCharacter
from rest_framework import viewsets, permissions
from .serializers import PlanetSerializer, CharacterSerializer, SpeciesSerializer, VehicleSerializer, StarshipSerializer, MovieSerializer, CharacterMovieSerializer, WildlifeSerializer, UserPlanetSerializer, UserWildlifeSerializer, UserCharacterSerializer

class PlanetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Planet.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlanetSerializer

class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Species.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SpeciesSerializer

class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Character.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CharacterSerializer

class VehicleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VehicleSerializer

class StarshipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Starship.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StarshipSerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer

class CharacterMovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CharacterMovie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CharacterMovieSerializer

class WildlifeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Wildlife.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WildlifeSerializer

class UserWildlifeViewSet(viewsets.ModelViewSet):
    # queryset = UserWildlife.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UserWildlifeSerializer

    def get_queryset(self):
        return self.request.user.userwildlife.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserCharacterViewSet(viewsets.ModelViewSet):
    # queryset = UserCharacter.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserCharacterSerializer

    def get_queryset(self):
        return self.request.user.usercharacters.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserPlanetViewSet(viewsets.ModelViewSet):
    # queryset = UserPlanet.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserPlanetSerializer
    
    def get_queryset(self):
        return self.request.user.userplanets.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)