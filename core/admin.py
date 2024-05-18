from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'user', 'created_date')
    list_filter = ('is_completed', 'created_date')
    search_fields = ('description', 'user__username')
