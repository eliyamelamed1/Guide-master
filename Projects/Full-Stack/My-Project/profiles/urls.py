from django.urls import path
from .views import (
    ProfileList,
    ProfileDetails,
    ProfileCreate,
    TopRatedChefsList,
)


urlpatterns = [
    path('', ProfileList.as_view()),
    path('<int:pk>/', ProfileDetails.as_view()),
    path('create/', ProfileCreate.as_view()),
    path('topratedchefs/', TopRatedChefsList.as_view()),
]
# TODO - change int to <uuid:pk>