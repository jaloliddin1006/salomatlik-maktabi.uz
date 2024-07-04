from django.contrib import admin
from apps.accounts.models import User, UserResetPassword
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
    list_display = ("username", "email", "first_name", "last_name", "phone", "birth", "is_staff")

@admin.register(UserResetPassword)
class UserResetPasswordCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', )
    list_display_links=('id', 'email', )
    