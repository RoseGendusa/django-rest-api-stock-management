from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="brands", default="default.png", null=True, blank=True)

    def __str__(self):
      return self.name
    
class UpdateCreateData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
class Product(UpdateCreateData):
    name = models.CharField(max_length=100, unique=True) # iPhone 11 
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    stock = models.IntegerField(blank=True, default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} --> {self.stock}"

class Firm(UpdateCreateData):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    image = models.ImageField(upload_to="firms", default="default.png", null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.name

class Purchase(UpdateCreateData):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    firm = models.ForeignKey(Firm, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.product} --- {self.quantity}"
    
    @property
    def price_total(self):
        return self.quantity * self.price
    

class Sale(UpdateCreateData):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.product} --- {self.quantity}"
    
    @property
    def price_total(self):
        return self.quantity * self.price

