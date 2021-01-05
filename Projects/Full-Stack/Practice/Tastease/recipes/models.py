from django.db import models
from django.utils.timezone import now
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
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='media/', blank=True)
    list_date = models.DateTimeField(default=now, blank=True) # TODO - improve

    def __str__(self):
        return self.title

