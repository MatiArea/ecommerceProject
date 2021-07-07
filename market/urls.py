from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('cart/', views.shop_cart, name='cart'),
    path('product/<int:id>', views.get_product, name='get_one_product'),
    path('product/', views.product, name='product'),
    path('product/new', views.new_product, name="product_new"),
    path('categories/', views.all_categories, name='all_acategories'),
    path('category/', views.category, name='category'),
    path('category/new', views.new_category, name='category_new'),
    path('aboutus/', views.about_us, name='about_us'),
]
