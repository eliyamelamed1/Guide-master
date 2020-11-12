from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # new
]


# path (url, ViewClassName.as_view, name='variableName')
# path (url, include(file.urls))