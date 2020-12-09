from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    # author = models.ForeignKey(User , on_delete=models.CASCADE) # a User can be an author of multiple blog posts
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/', blank=True)
    trending = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    
# TODO - set id as uuid
# id = models.UUIDField( # set id field to be a UUIDField that is now the primary key
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False)