from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'method_type', 'flavor_type', 'difficulty_type', 'prep_time', 'photo_main')