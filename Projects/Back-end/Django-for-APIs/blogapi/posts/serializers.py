from rest_framework import serializers
from .models import Post


# Post details
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at')
        model = Post



# serializer transforms data into JSON, and can specify which fields to include/exclude
