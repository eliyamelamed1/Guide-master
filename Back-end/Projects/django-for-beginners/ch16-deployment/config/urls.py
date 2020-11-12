from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # linking to the built in admin.site
    path('accounts/', include('accounts.urls')), # linking to a file that contain's 'urlpattenrs'
    path('accounts/', include('django.contrib.auth.urls')), # provide a built in auth (users) features 
    path('articles/', include('articles.urls')), 
    path('', include('pages.urls')),
]


# the built in 'auth' app, provides a User object containing:
# • username
# • password
# • email
# • first_name
# • last_name

# • registaration templates
# have built in login page + form - templates/registration/login.html