from django.shortcuts import render, redirect
from django.http import HttpResponse
from market.models import Product, Category
from django import template

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 


def index(request):
    # try:
        products = Product.objects.all().order_by("-id")[:10]
        context = {'first': products[0:3],
                   'second': products[4:10]
                   }
        print(products)
        return render(request, 'home.html', context)
    # except:
    #     return HttpResponse(404)


def product(request):
    categories = Category.objects.all()
    context = {
        "allCategories": categories
    }
    return render(request, 'product/new_product.html', context)


def category(request):
    return render(request, 'category/new_category.html')


def new_product(request):
    try:
        new_product = Product()
        new_product.tittle = request.POST.get('name')
        new_product.description = request.POST.get('description')
        new_product.price = request.POST.get('price')
        new_product.url_image = request.POST.get('img')
        new_product.category_id = Category.objects.get(
            id=request.POST.get('category'))
        new_product.save()
        return redirect('/market/home')
    except:
        return HttpResponse(404)


def new_category(request):
    new_category = Category()
    new_category.description = request.POST.get('description')
    new_category.save()
    return redirect('/market/home')


def all_categories(request):
    categories = Category.objects.all()
    return categories


def about_us(request):
    return render(request, 'about_us.html')


def get_product(request,id):
    try:
        product = Product.objects.get(id=id)
        context = {
            'product':product,
        }
        print(product.category_id.description)
        return render(request, 'product/view_product.html',context)
    except:
        return HttpResponse(404)


def shop_cart(request):
    return render(request, 'shop_cart.html')
