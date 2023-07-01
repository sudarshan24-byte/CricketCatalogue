from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Players)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'team', 'country')