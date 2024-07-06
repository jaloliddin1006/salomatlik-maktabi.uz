from django.contrib import admin
from apps.home.models import Contact, Subscribe
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    search_fields = ['name', 'email']
    list_filter = ['created_at']
    
@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    list_filter = ['created_at']
