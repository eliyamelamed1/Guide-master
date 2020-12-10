from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, generics
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 
    pagination_class = None

class ProfileDetails(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 

class ProfileCreate(CreateAPIView):
    permissions_classes = (permissions.IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TopRatedChefsList(ListAPIView):
    queryset = Profile.objects.filter(top_rated_chef=True)
    serializer_class = ProfileSerializer 
    pagination_class = None