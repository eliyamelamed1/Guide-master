from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
]


# path(url, viewName.as_view, name='variableName')