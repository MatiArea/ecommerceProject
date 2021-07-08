from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('cart/', views.shop_cart, name='cart'),
    path('product/<int:id>', views.get_product, name='get_one_product'),
    path('product/new', views.new_product, name="product_new"),
    path('product/edit/<int:id>', views.edit_product, name="product_edit"),
    path('product/delete/<int:id>', views.delete_product, name="product_delete"),
    path('category/all', views.all_categories, name='all_acategories'),
    path('category/new', views.new_category, name='category_new'),
    path('aboutus/', views.about_us, name='about_us'),
]
