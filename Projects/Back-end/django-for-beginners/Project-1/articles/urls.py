from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView, # new
    ArticleDetailView, # new
    ArticleDeleteView, # new
    ArticleCreateView, # new
)

urlpatterns = [
    path('<int:pk>/edit/',
         ArticleUpdateView.as_view(), name='article_edit'),  # linking viewModel to a url, url is base on object.pk/object.id - used in templates/file.html <a href="{% url 'variableName' object.pk %}"></a>
    path('<int:pk>/',
         ArticleDetailView.as_view(), name='article_detail'), 
    path('<int:pk>/delete/',
         ArticleDeleteView.as_view(), name='article_delete'), # linking a viewModel and a url location, and saving the whole path on a variabel
    path('new/', ArticleCreateView.as_view(), name='article_new'), 
    path('', ArticleListView.as_view(), name='article_list'),
]

