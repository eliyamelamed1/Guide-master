from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'middle_name', 'last_name', 'about_me', 'profile_photo', 'updated_at',) 

