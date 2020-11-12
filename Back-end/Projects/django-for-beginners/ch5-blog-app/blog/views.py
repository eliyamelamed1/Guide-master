from django.views.generic import ListView, DetailView # new
from .models import Post

DetailView # will provide a context object we can use in our template called either object or the lowercased name of our model


class BlogListView(ListView):
    model = Post # linking to a the model
    template_name = 'home.html' # linking to an html file


class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'
