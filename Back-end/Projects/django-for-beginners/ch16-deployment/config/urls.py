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

# • built in registaration templates (in order to modify built in templates just create a template with the same name and path)

# login template + form - templates/registration/login.html or templates/accounts/login.html

# password change template + form - templates/registration/password_change_form.html 
# password changed template + form - templates/registration/password_change_done.html 

# password reset template + form - templates/registration/password_reset_form.html 
# password reset sent to email template + form - templates/registration/password_reset_dont.html 
# template that sent to user email with their details and paswword reset confirm link - templates/registration/password_reset_email.html
# link to confirm you are the user owner - templates/registration/password_reset_confirm.html
# password reset complete - templates/registration/password_reset_complete.html

 # modify this file to change email password reset text - templates/registration/password_reset_subject.txt
