from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # linking a viewModel to an url location, and saving the whole path as a variable
]
