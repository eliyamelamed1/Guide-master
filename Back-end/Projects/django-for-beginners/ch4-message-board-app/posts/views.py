from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post # linking the model
    template_name = 'home.html' # linking the html file
    context_object_name = 'all_posts_list' # new
