from django.shortcuts import render
from .models import Product, BlogPost


def home(request):
    return render(request, 'website/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'website/products.html', {'products': products})

def blog_list(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'website/blogs.html', {'blogposts': blogposts})