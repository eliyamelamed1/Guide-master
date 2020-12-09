from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, generics
from .models import Post
from .serializers import PostSerializer

class PostsList(ListAPIView):
    permissions_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    pagination_class = None

class PostDetails(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class PostCreate(CreateAPIView):
    permissions_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TrendingPosts(ListAPIView):
    permissions_classes = (permissions.AllowAny,)
    queryset = Post.objects.filter(trending=True)
    serializer_class = PostSerializer 
    pagination_class = None