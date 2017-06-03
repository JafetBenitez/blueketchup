#from django.shortcuts import render
from core.models import Tag, Dish, Profile, Restaurant, Franchise
from rest_framework import viewsets
from core.serializers import TagSerializer, DishSerializer, ProfileSerializer, RestaurantSerializer, FranchiseSerializer
# Create your views here.

class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint  for qualities of restaurants, franchises and dishes
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class DishViewSet(viewsets.ModelViewSet):
    """
    API endpoint  for qualities of restaurants, franchises and dishes
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint  for qualities of restaurants, franchises and dishes
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint  for qualities of restaurants, franchises and dishes
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class FranchiseViewSet(viewsets.ModelViewSet):
    """
    API endpoint  for qualities of restaurants, franchises and dishes
    """
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer
