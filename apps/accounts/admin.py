from django.contrib import admin
from apps.accounts.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("email", "password1", "password2", "username"),
                },
            ),
        )