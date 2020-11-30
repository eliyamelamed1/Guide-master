from django.contrib.auth.models import AbstractUser
from django.db import models

# CustomUser now has inherited all the functionality of AbstractUser, but we can override or add new functionality as needed.
class CustomUser(AbstractUser):
    pass
