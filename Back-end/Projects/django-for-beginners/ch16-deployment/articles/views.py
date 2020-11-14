from django.contrib.auth.mixins import (
    LoginRequiredMixin, # give permission only to logged in users
    UserPassesTestMixin # restrict access from other users so that only the author have this permission
)
from django.views.generic import (
    ListView,  # to display multiple posts
    DetailView # provide a context object we can use in our template called either object or the lowercased name of our model
)# new
from django.views.generic.edit import ( 
    UpdateView, # update post
    DeleteView, # delete post
    CreateView  # create post
) 
from django.urls import reverse_lazy # new
from .models import Article

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

    # if the author of the current object(post) matches the current user on the webpage , then give him permission (allow him to update the post)
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    # if the author of the current object(post) matches the current user on the webpage , then give him permission (allow him to delete the post)
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView): # new
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body') 

    # function to determine that new post will be automatically set to the current user as the post's author. 
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)


# success_url =  choose path to redirect when method executed
# reverse_lazy('pathVariableName')=  We use reverse_lazy as opposed to just reverse so that it won’t execute the URL redirect until our view has finished deleting the blog post