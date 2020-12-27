from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions
from .models import Recipe
from .serializers import RecipeSerializer, RecipeSearchSerializer
from datetime import datetime, timezone, timedelta

class RecipeList(ListAPIView):
    queryset = Recipe.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = RecipeSerializer

class RecipeDetail(RetrieveAPIView):
    queryset = Recipe.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = RecipeSerializer

class RecipeCreate(CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
class RecipeSearch(APIView):
    serializer_class = Recipe.objects.all()

    def post(self, request, format=None):
        queryset = Recipe.objects.order_by('-list_date').filter(is_published=True)
        data = self.request.data

        method_type = data['method_type']
        queryset = queryset.filter(method_type__iexact=method_type)
        
        flavor_type = data['flavor_type']
        queryset = queryset.filter(flavor_type__iexact=flavor_type)

        difficulty_type = data['difficulty_type']
        queryset = queryset.filter(difficulty_type__iexact=difficulty_type)

        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)

        serializer = RecipeSearchSerializer(queryset, many=True)

        return Response(serializer.data)
