from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Declaring Article attributes
class Article(models.Model):
    title = models.CharField(max_length=255) # limits the title's length to 200 characters
    body = models.TextField() #  TextField - text box that streches based on the user’s text
    date = models.DateTimeField(auto_now_add=True) # saves the current date & time
    author = models.ForeignKey( # ForeignKey- "allows for a many-to-one relationship." - a given user can be the author of many different blog posts but not the other way around.
        get_user_model(), # This method will set the current user as the author 
        on_delete=models.CASCADE,
    )

    # a function that display the object title as the object name .- for example check the admin panel
    def __str__(self):
        return self.title 
    
    # get the url path of -  article_detail_url_path/object.id 
    def get_absolute_url(self): 
        return reverse('article_detail', args=[str(self.id)]) # return an object id to a url path's via varaiableName


class Comment(models.Model): 
    article = models.ForeignKey(  
        Article, # Articles can have multiple comments but not the other way around
        on_delete=models.CASCADE,
        related_name='comments', # Set the name comments to be the name of the entire Comment model. (used in template/article_list.html)
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(), # a user can have multiple comments but not the other way around
        on_delete=models.CASCADE,
    )

     
    def __str__(self):
        return self.comment 

    # get the url path of -  article_list_url_path 
    def get_absolute_url(self):
        return reverse('article_list')  
