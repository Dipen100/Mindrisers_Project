from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'username', 'role'
    ]
    ordering = ('id',)