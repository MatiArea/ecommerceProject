from django.shortcuts import render, redirect
from django.http import HttpResponse
from market.models import Product, Category
from django.contrib.auth.models import User, Group


def index(request):
    try:
        products = Product.objects.all().order_by("-id")[:10]
        context = {'first': products[0:3],
                   'second': products[4:10]
                   }
        print(products)
        return render(request, 'home.html', context)
    except:
        return HttpResponse(404)


def register(request):
    if request.method == 'POST':
        if(request.POST.get('contrasena') == request.POST.get('contrasena2')):
            user = request.POST.get('username')
            password = request.POST.get('contrasena')
            email = request.POST.get('email')
            new_user = User.objects.create_user(user, email, password)
            my_group = Group.objects.get(name='usuario')
            new_user.groups.add(my_group)
            new_user.save()
            return redirect('/accounts/login')
    else:
        return render(request, 'register.html')


def new_product(request):
    if request.method == 'POST':
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
            return HttpResponse(500)
    else:
        categories = Category.objects.all()
        context = {
            "allCategories": categories
        }
        return render(request, 'product/new_product.html', context)


def edit_product(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=id)
            product.tittle = request.POST.get('name')
            product.description = request.POST.get('description')
            product.price = request.POST.get('price')
            product.url_image = request.POST.get('img')
            product.category_id = Category.objects.get(
                id=request.POST.get('category'))
            product.save()
            return redirect('/market/home')
        except:
            return HttpResponse(404)
    else:
        categories = Category.objects.all()
        product_to_edit = Product.objects.get(id=id)
        context = {
            "product_to_edit": product_to_edit,
            "allCategories": categories
        }
        return render(request, 'product/edit_product.html', context)


def delete_product(request, id):
    try:
        product_to_delete = Product.objects.get(id=id)
        product_to_delete.delete()
        return redirect('/market/home')
    except:
        return HttpResponse(404)


def new_category(request):
    if request.method == 'POST':
        new_category = Category()
        new_category.description = request.POST.get('description')
        new_category.save()
        return redirect('/market/home')
    else:
        return render(request, 'category/new_category.html')


def all_categories(request):
    categories = Category.objects.all()
    return categories


def about_us(request):
    return render(request, 'about_us.html')


def get_product(request, id):
    try:
        product = Product.objects.get(id=id)
        context = {
            'product': product,
        }
        return render(request, 'product/view_product.html', context)
    except:
        return HttpResponse(404)


def search(request):
    values = request.GET.get('search')
    products = Product.objects.filter(tittle__contains=values)
    products.union(Product.objects.filter(description__contains=values))
    context = {'products': products}
    return render(request, 'product/list_product.html', context)


def shop_cart(request):
    return render(request, 'shop_cart.html')
