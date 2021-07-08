from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    description = models.CharField(max_length=150)
    class Meta:  
        db_table = "Category"


class Product(models.Model):
    tittle = models.CharField(max_length=40, null=False)
    description = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2,max_digits=10,null=False)
    photo = models.ImageField(upload_to='images',default='null')
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False)
    class Meta:  
        db_table = "Product"

class ShopCart(models.Model):
    totalSale = models.DecimalField(decimal_places=2,max_digits=10, null=False)
    user_id = models.ForeignKey(User,on_delete = models.SET_NULL,null=True)
    class Meta:  
        db_table = "Shop_cart"

class Product_Cart(models.Model):
    amount = models.IntegerField()
    product_id = models.ForeignKey(Product,on_delete = models.SET_NULL,null=True)
    cart_id = models.ForeignKey(ShopCart,on_delete = models.SET_NULL,null=True)
    class Meta:  
        db_table = "Employee"