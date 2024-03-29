from django.urls import path
# from .views import PostList, PostDetail, UserList, UserDetail
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet


# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('users/', UserList.as_view()),
# ]


# Routers work directly with viewsets to automatically generate URL patterns for us.
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls