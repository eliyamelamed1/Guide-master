from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeCreate, RecipeSearch

urlpatterns = [
    path('', RecipeList.as_view()),
    path('create/', RecipeCreate.as_view()),
    path('<uuid:pk>/', RecipeDetail.as_view() ),
    path('search/', RecipeSearch.as_view()),
]
