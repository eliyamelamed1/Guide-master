from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # User management
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('dj_rest_auth.urls')),
    path('signup', include('dj_rest_auth.registration.urls')),
   
    # Local
    path('profile/', include('profiles.urls')),
    path('recipes/', include('recipes.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))] # catch all other routes that not specified in this file

# dj_rest_auth includes:
    # login - /login
    # logout - /logout
    # password reset - /password/reset
    # password confirm - /password/reset/confirm


# path('accounts/', include('allauth.urls')),