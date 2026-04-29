from django.contrib import admin
from .models import Product, BlogPost

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog')

