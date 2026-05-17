from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST

from .models import Product, BandA, BlogPost, Review
from .forms import ProductForm, BandAForm, BlogForm


# =========================================================
# Helper Function
# =========================================================

def staff_required(user):
    return user.is_authenticated and user.is_staff


# =========================================================
# Home Page
# =========================================================

def home(request):
    return render(request, 'website/home.html')


# =========================================================
# Products
# =========================================================

def product_page(request):
    products = Product.objects.all().order_by('-id')
    bandAs = BandA.objects.all().order_by('-id')

    context = {
        'products': products,
        'bandAs': bandAs,
    }

    return render(request, 'website/products.html', context)


@login_required
def make_product(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully.")
            return redirect('products')

    else:
        form = ProductForm()

    context = {
        'form': form,
        'page_title': 'Create Product'
    }

    return render(request, 'website/makeProduct.html', context)


@login_required
def update_product(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect('products')

    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
        'page_title': 'Update Product'
    }

    return render(request, 'website/updateProduct.html', context)


@login_required
@require_POST
def delete_product(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    product = get_object_or_404(Product, pk=pk)
    product.delete()

    messages.success(request, "Product deleted successfully.")
    return redirect('products')


# =========================================================
# Before & After
# =========================================================

@login_required
def make_BandA(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    if request.method == "POST":
        form = BandAForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Before & After entry created successfully.")
            return redirect('products')

    else:
        form = BandAForm()

    context = {
        'form': form,
        'page_title': 'Create Before & After'
    }

    return render(request, 'website/makeBandA.html', context)


@login_required
def update_BandA(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    banda = get_object_or_404(BandA, pk=pk)

    if request.method == "POST":
        form = BandAForm(request.POST, request.FILES, instance=banda)

        if form.is_valid():
            form.save()
            messages.success(request, "Before & After entry updated successfully.")
            return redirect('products')

    else:
        form = BandAForm(instance=banda)

    context = {
        'form': form,
        'banda': banda,
        'page_title': 'Update Before & After'
    }

    return render(request, 'website/updateBandA.html', context)


@login_required
@require_POST
def delete_BandA(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    banda = get_object_or_404(BandA, pk=pk)
    banda.delete()

    messages.success(request, "Before & After entry deleted successfully.")
    return redirect('products')


# =========================================================
# Blog Posts
# =========================================================

def blog_page(request):
    blogposts = BlogPost.objects.all().order_by('-id')

    context = {
        'blogposts': blogposts
    }

    return render(request, 'website/blogs.html', context)


@login_required
def make_blogpost(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Blog post created successfully.")
            return redirect('blogs')

    else:
        form = BlogForm()

    context = {
        'form': form,
        'page_title': 'Create Blog Post'
    }

    return render(request, 'website/makeBlog.html', context)


@login_required
def update_blogpost(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    blogpost = get_object_or_404(BlogPost, pk=pk)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blogpost)

        if form.is_valid():
            form.save()
            messages.success(request, "Blog post updated successfully.")
            return redirect('blogs')

    else:
        form = BlogForm(instance=blogpost)

    context = {
        'form': form,
        'blogpost': blogpost,
        'page_title': 'Update Blog Post'
    }

    return render(request, 'website/updateBlog.html', context)


@login_required
@require_POST
def delete_blogpost(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    blogpost = get_object_or_404(BlogPost, pk=pk)
    blogpost.delete()

    messages.success(request, "Blog post deleted successfully.")
    return redirect('blogs')


# =========================================================
# Reviews
# =========================================================

def reviews_page(request):
    reviews = Review.objects.all().order_by('-created_at')

    rating_filter = request.GET.get('rating')

    if rating_filter and rating_filter.isdigit():
        reviews = reviews.filter(rating=int(rating_filter))

    context = {
        'reviews': reviews,
        'selected_rating': rating_filter
    }

    return render(request, 'website/reviews.html', context)


@require_POST
def add_review(request):
    name = request.POST.get('name', '').strip()
    rating = request.POST.get('rating', '').strip()
    comment = request.POST.get('comment', '').strip()

    # Validation
    if not name or not rating or not comment:
        messages.error(request, "All fields are required.")
        return redirect('reviews_page')

    try:
        rating = int(rating)

        if rating < 1 or rating > 5:
            messages.error(request, "Rating must be between 1 and 5.")
            return redirect('reviews_page')

    except ValueError:
        messages.error(request, "Invalid rating.")
        return redirect('reviews_page')

    Review.objects.create(
        name=name,
        rating=rating,
        comment=comment
    )

    messages.success(request, "Review submitted successfully.")

    return redirect('reviews_page')