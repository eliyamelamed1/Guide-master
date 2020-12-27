from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('recipes/', include('recipes.urls')),
    path('users/', include('dj_rest_auth.urls')), 
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]


# djoser.urls includes:
    # /users/
    # /users/me/
    # /users/confirm/
    # /users/resend_activation/
    # /users/set_password/
    # /users/reset_password/
    # /users/reset_password_confirm/
    # /users/set_username/
    # /users/reset_username/
    # /users/reset_username_confirm/

# dj_rest_auth includes:
    # login - /login
    # logout - /logout
    # password reset - /password/reset
    # password confirm - /password/reset/confirm

