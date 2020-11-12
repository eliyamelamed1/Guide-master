from django.db import models


# Declaring post attributes
class Post(models.Model):
    title = models.CharField(max_length=200) # limits the length to 200 characters

    author = models.ForeignKey ( # ForeignKey- "allows for a many-to-one relationship." - a given user can be the author of many different blog posts but not the other way around.
        'auth.User', # The reference is to the built-in User model that Django provides for authentication
        on_delete=models.CASCADE, 
    )
    body = models.TextField() #  TextField based on the user’s text

    def __str__(self):
        return self.title


