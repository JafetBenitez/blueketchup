from core.models import Tag, Franchise, Profile, Restaurant, Dish
from rest_framework import serializers


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name', 'created_date')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'franchise', 'restaurant', 'created_by', 'created_date')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('users', 'tags', 'franchise', 'created_date')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'franchise', 'latitude','longitude','description','reference', 'phone','tags', 'created_by', 'created_date')


class FranchiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Franchise
        fields = ('name', 'description', 'tags', 'created_by', 'created_date')
