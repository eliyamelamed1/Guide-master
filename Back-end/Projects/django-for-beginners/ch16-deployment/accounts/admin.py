from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# be able to control users via the admin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm # add creation form
    form = CustomUserChangeForm # change form
    model = CustomUser 
    list_display = ['email', 'username', 'age', 'is_staff', ] # attributes to display on the admin
    fieldsets = UserAdmin.fieldsets + ( # new
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( # new
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin) # display apps and its database's model Post on the admin page
