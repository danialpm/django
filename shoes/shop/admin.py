from django.contrib import admin
from .models import Shop

# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'publish',)
    list_filter = ('created', 'publish', 'user')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('publish',)