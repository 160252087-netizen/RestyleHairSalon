from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    name = models.CharField(max_length=200)
    blog = models.TextField()
    image = models.ImageField(upload_to='blogs/')

    def __str__(self):
        return self.name
    
class BandA(models.Model):
    name = models.CharField(max_length=200)
    before = models.ImageField(upload_to='products/')
    after = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

