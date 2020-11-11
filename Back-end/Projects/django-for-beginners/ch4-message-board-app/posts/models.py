from django.db import models


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50] # display the first 50 characters of the text field as the object name in the admin
