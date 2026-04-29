from django.urls import path
from . import views

urlpatterns = [
    # - Homepage
    path('', views.home, name=""),

    # - Products
    path('products/', views.product_page, name='products'),
    path('make_products/', views.make_product, name='make_products'),
    path('update_products/', views.update_product, name='update_products'),
    path('make_BandA/', views.make_BandA, name='make_BandA'),
    path('update_BandA/', views.update_BandA, name='update_BandA'),

    # - Blog Posts
    path('blog/', views.blog_page, name='blogs'),
    path('make_blog/', views.make_blogpost, name='make_blog'),
    path('update_blog/', views.update_blogpost, name='update_blog'),

    # - Reviews
    path('reviews/', views.reviews_page, name='reviews_page'),
    path('add-review/', views.add_review, name='add_review'),
]