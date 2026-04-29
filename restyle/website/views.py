from django.shortcuts import render, redirect
from .models import Product, BandA, BlogPost, Review
from .forms import ProductForm, BandAForm, BlogForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# - Home Page
def home(request):
    return render(request, 'website/home.html')

# - Products
def product_page(request):
    products = Product.objects.all()
    bandAs = BandA.objects.all()
    
    return render(request, 'website/products.html', {'products': products,
    'bandAs' : bandAs})

@login_required
def make_product(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    
    context = {'form': form}

    return render(request, 'website/makeProduct.html', context=context)

@login_required
def update_product(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    return render(request, 'website/updateProduct.html')

@login_required
def make_BandA(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    
    form = BandAForm()

    if request.method == "POST":
        form = BandAForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
        
    context = {'form': form}

    return render(request, 'website/makeBandA.html', context=context)

@login_required
def update_BandA(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    return render(request, 'website/updateBandA.html')


# - Blog Posts
def blog_page(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'website/blogs.html', {'blogposts': blogposts})

@login_required
def make_blogpost(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()

    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs')
        
    context = {'form': form}

    return render(request, 'website/makeBlog.html', context=context)

@login_required
def update_blogpost(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    return render(request, 'website/updateBlog.html')

def reviews_page(request):
    reviews = Review.objects.all().order_by('-created_at')

    rating_filter = request.GET.get('rating')
    if rating_filter:
        reviews = reviews.filter(rating=rating_filter)

    return render(request, 'website/reviews.html', {'reviews': reviews})


def add_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            name=name,
            rating=rating,
            comment=comment
        )

    return redirect('reviews_page')

