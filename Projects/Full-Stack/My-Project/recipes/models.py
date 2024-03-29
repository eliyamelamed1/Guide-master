from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
import uuid

class Recipe(models.Model):
    class MethodType(models.TextChoices):
        COOK = 'Cook'
        BAKE = 'Bake'
    
    class FlavorType(models.TextChoices):
        SOUR = 'Sour'
        SWEET = 'Sweet'
        SALTY = 'Salty'
    
    class DifficultyType(models.TextChoices):
        EASY = 'Easy'
        INTERMEDIATE = 'Intermediate'
        HARD = 'Hard'

    id = models.UUIDField( # set id field to be a UUIDField that is now the primary key
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    method_type = models.CharField(max_length=50, choices=MethodType.choices, default=None)
    flavor_type = models.CharField(max_length=50, choices=FlavorType.choices, default=None)
    difficulty_type = models.CharField(max_length=50, choices=DifficultyType.choices, default=None)
    # prep_time = models.IntegerField()
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='media/', blank=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title

