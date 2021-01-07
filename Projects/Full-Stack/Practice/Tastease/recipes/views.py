from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import permissions

from .models import Recipe
from .serializers import RecipeSerializer, RecipeSearchSerializer

class RecipeList(ListAPIView):
    queryset = Recipe.objects.order_by('-updated_at')
    serializer_class = RecipeSerializer

class RecipeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.order_by('-updated_at')
    serializer_class = RecipeSerializer

class RecipeCreate(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
class RecipeSearch(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = RecipeSearchSerializer

    def post(self, request, format=None):
        queryset = Recipe.objects.order_by('-updated_at')
        data = self.request.data

        description = data['description']
        queryset = queryset.filter(description__icontains=description)

        flavor_type = data['flavor_type']
        queryset = queryset.filter(flavor_type__iexact=flavor_type)

        serializer = RecipeSerializer(queryset, many=True)

        return Response(serializer.data)
        