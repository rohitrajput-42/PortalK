from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, default='', null = True, blank = True)
    eligibilty = models.CharField(max_length=150)
    image = models.ImageField(upload_to="upload/products/")
    location = models.CharField(max_length = 100)

    
    @staticmethod
    def get_all_products():
        return Product.objects.all

    def __str__(self):
        return self.name