from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'bio',
        'is_staff'
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("bio",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("bio",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
