from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name',)
    list_display_links = ('id', 'first_name',)
    search_fields = ('first_name',)
    list_per_page = 25

admin.site.register(Profile, ProfileAdmin)