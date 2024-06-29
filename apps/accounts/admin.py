from django.contrib import admin
from apps.accounts.models import User, UserResetPasswordCode
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

@admin.register(UserResetPasswordCode)
class UserResetPasswordCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'email', 'expiration_time', 'is_confirmation',)
    list_display_links=('id', 'code', 'email', 'expiration_time',)
    