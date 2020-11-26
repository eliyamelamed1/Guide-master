from django.contrib.auth.models import AbstractUser
from django.db import models

# a new User model which we’ll call CustomUser that extendsthe existing AbstractUser. 

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

# • null is database-related. When a field has null=True it can store a database entry as NULL,
# meaning no value.
# • blank is validation-related, if blank=True then a form will allow an empty value, whereas
# if blank=False then a value is required.

# In practice, null and blank are commonly used together in this fashion so that a form allows an
# empty value and the database stores that value as NULL.
# A common gotcha to be aware of is that the field type dictates how to use these values. Whenever
# you have a string-based field like CharField or TextField, setting both null and blank as we’ve
# done will result in two possible values for “no data” in the database. Which is a bad idea. The
# Django convention is instead to use the empty string '', not NULL.
