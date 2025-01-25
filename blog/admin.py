#from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description')
    search_fields = ('name',)

"""@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('Post', 'caption', 'uploaded_at')
    list_filter = ('Post', 'uploaded_at')
"""
