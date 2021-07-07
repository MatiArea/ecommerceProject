from market.models import Product_Cart, ShopCart, Category, Product
from django.contrib import admin

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShopCart)
admin.site.register(Product_Cart)
