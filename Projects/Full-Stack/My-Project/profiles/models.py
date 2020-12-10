from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    # author = models.ForeignKey(User , on_delete=models.CASCADE) # a User can be an author of multiple blog posts
    id = models.UUIDField( # set id field to be a UUIDField that is now the primary key
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    about_me = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='media/', blank=True)
    top_rated_chef = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name # change to full name
