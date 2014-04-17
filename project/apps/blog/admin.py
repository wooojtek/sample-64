from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'created', 'published']
    list_filter = ['category', 'published']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)