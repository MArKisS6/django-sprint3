from django.contrib import admin
from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'is_published',
        'category',
        'author',
        'location',
        'created_at'
    )
    list_editable = (
        'is_published',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('is_published', 'category', 'location')
    list_display_links = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)


admin.site.register(Post, PostAdmin)
