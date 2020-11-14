from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

# creating sign up module - all of the other modules are build in Django 
class SignUpView(CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login') # redirect to login when sign up is finished
    template_name = 'registration/signup.html'
