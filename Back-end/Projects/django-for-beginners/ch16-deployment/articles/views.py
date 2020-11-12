from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from .models import Article

# ListView - display multiple posts
# DetailView - will provide a context object we can use in our template called either object or the lowercased name of our model
# CreateView - create post
# UpdateView - update post
# DeleteView - delete post

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article # linking to a the model
    template_name = 'article_list.html' # linking to a template html file 


class ArticleDetailView(LoginRequiredMixin, DetailView): # new
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Article
    fields = ('title', 'body',) # update this attributes of blog post
    template_name = 'article_edit.html'

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView): # new
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body') # new

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)


# success_url=  choose path to redirect when method executed
# reverse_lazy('pathVariableName')=  We use reverse_lazy as opposed to just reverse so that it won’t execute the URL redirect until our view has finished deleting the blog post