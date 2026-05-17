from django.urls import path
from . import views

urlpatterns = [
    # - Homepage
    path('', views.home, name=""),

    # - Products
    path('products/', views.product_page, name='products'),
    path('make_product/', views.make_product, name='make_product'),
    path('products/update/<int:pk>/', views.update_product, name='update_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),

    path('make_BandA/', views.make_BandA, name='make_BandA'),
    path('banda/update/<int:pk>/', views.update_BandA, name='update_BandA'),
    path('banda/delete/<int:pk>/', views.delete_BandA, name='delete_BandA'),


    # - Blog Posts
    path('blog/', views.blog_page, name='blogs'),
    path('make_blog/', views.make_blogpost, name='make_blog'),
    path('blogs/update/<int:pk>/', views.update_blogpost, name='update_blogpost'),
    path('blogs/delete/<int:pk>/', views.delete_blogpost, name='delete_blogpost'),

    # - Reviews
    path('reviews/', views.reviews_page, name='reviews_page'),
    path('add-review/', views.add_review, name='add_review'),
]