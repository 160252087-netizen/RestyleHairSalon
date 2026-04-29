from django.contrib import admin
from .models import Product, BlogPost, BandA

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog')

@admin.register(BandA)
class BandAAdmin(admin.ModelAdmin):
    list_display = ('name', 'before', 'after')

