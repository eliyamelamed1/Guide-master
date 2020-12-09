from django.urls import path
from .views import (
    PostsList,
    PostDetails,
    PostCreate,
    TrendingPosts,
)


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', PostDetails.as_view()),
    path('create/', PostCreate.as_view()),
    path('trending/', TrendingPosts.as_view()),
]
# TODO - change int to <uuid:pk>