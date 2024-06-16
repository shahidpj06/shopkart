from django.db import models

# for creating the details of product
class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    priority = models.IntegerField(default=0) # changes when season changes
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE) # deletion will be temperary
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f"{self.product.title} Image"