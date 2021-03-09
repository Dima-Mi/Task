from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import Category, Store, Warehouse, Product, Catalog
from .forms import LoginForm, UserRegisterForm, UserLoginForm


def login_check(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('sales:login'))

    return wrapper


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    shop = Store.objects.all()
    warehouse = Warehouse.objects.all()
    products = Product.objects.all().order_by('-created')
    sales_list = Catalog.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'sales/product/list.html',
                  {'category': category, 'categories': categories, 'sales_list': sales_list,
                   'products': products, 'shop': shop, 'warehouse': warehouse,
                   })


@login_check
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    catalog = Catalog.objects.filter(products=product)
    return render(request, 'sales/product/detail.html', {'product': product, 'catalog': catalog})


@login_check
def store_detail(request, slug):
    store = get_object_or_404(Store, slug=slug)
    products = Product.objects.filter(store=store)
    return render(request, 'sales/product/store.html', {'store': store, 'products': products})


@login_check
def warehouse_detail(request, slug):
    warehouse = get_object_or_404(Warehouse, slug=slug)
    store = Store.objects.filter(warehouse=warehouse)
    catalog = Catalog.objects.filter(warehouse=warehouse)
    return render(request, 'sales/product/warehouse.html', {'warehouse': warehouse, 'catalog': catalog, 'store': store})


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sales:product_list')
    else:
        form = UserRegisterForm()
    return render(request, 'sales/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('sales:product_list')
    else:
        form = UserLoginForm()
    return render(request, 'sales/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('sales:product_list')
