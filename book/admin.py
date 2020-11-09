from django.contrib import admin
from .models import Category, Book
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_field = {'slug': ('name',)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'price', 'image', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'created', 'updated']
    prepopulated_field = {'slug': ('title',)}

