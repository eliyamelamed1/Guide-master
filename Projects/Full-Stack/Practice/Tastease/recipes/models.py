from django.db import models
from django.contrib.auth import get_user_model
import uuid

class Recipe(models.Model):
    class FlavorType(models.TextChoices):
        SOUR = 'Sour'
        SWEET = 'Sweet'
        SALTY = 'Salty'

    id = models.UUIDField( 
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE) # TODO - change author to profile
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    flavor_type = models.CharField(max_length=50, choices=FlavorType.choices)
    photo_main = models.ImageField(upload_to='media/', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

