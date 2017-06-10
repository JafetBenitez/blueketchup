from core.models import Tag, Franchise, Profile, Restaurant, Dish
from rest_framework import serializers


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'franchise', 'restaurant')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('users', 'tags', 'franchise')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'franchise', 'latitude','longitude','description','reference', 'phone','tags')


class FranchiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Franchise
        fields = ('name', 'description', 'tags')
