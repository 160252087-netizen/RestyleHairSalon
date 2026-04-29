from django import forms
from .models import Product, BlogPost, BandA

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['name', 'blog', 'image']

class BandAForm(forms.ModelForm):
    class Meta:
        model = BandA
        fields = ['name', 'before', 'after'] 