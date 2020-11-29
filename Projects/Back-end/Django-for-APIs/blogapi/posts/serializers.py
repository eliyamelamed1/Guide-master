# serializer.py transforms data into JSON, and can specify which fields to include/exclude
from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model


# Post details
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)