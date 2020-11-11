from django.contrib import admin

from .models import Post

admin.site.register(Post) # display our posts app and its database model Post on the admin page

