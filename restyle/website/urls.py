from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),

    path('products/', views.product_list, name='products'),

    path('blog/', views.blog_list, name='blogs'),
]