from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Detail view page- Create Post
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Detail view page- Read,Update Delete Post.
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Create your views here.
