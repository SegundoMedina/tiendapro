from django.db import models

# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    weight = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="products_thumbs")
    image = models.ImageField(upload_to="products_images/")
    create_date = models.DateField()
    stock = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.category.name + " > " + self.product.name