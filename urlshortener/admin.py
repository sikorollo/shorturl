from django.contrib import admin
from .models import Shortener

@admin.register(Shortener)
class Shortener(admin.ModelAdmin):
    fields = ['created_date', 'visits', 'user_url', 'short_url']
    list_display = ['created_date', 'visits', 'user_url', 'short_url']
    date_hierarchy = 'created_date'
