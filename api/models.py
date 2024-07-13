from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=100)
    books_count = models.IntegerField()
    image = models.ImageField(upload_to='writers/', null=True, blank=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    books_count = models.IntegerField()
    image = models.ImageField(upload_to='publishers/', null=True, blank=True)

    def __str__(self):
        return self.name

# existing models remain unchanged
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    writer = models.CharField(max_length=100, default='Unknown Writer')
    publication = models.CharField(max_length=100, default='Unknown Publication')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    pdf = models.FileField(upload_to='products/pdfs/', null=True, blank=True)

    def __str__(self):
        return self.name
