import datetime
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *
from .forms import AddressForm, QuestionForm, SignUpForm
from .utils import cartData


def index(request):
    beverages = Product.objects.filter(category=Category.objects.get(name='Напитка').id)
    foods = Product.objects.filter(category=Category.objects.get(name='Еда').id)

    if request.user.is_authenticated:
        data = cartData(request)
        cartItems = data['cartItems']
    else:
        cartItems = 0

    context = {
        'title': 'Главная',
        'beverages': beverages,
        'foods': foods,
        'cartItems': cartItems,
    }
    return render(request, 'mainapp/index.html', context)


def cart(request):
    data = cartData(request)

    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {
        'title': 'Корзина',
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'mainapp/cart.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            Customer.objects.create(user=user, name=form.cleaned_data['username'],
                                    email=form.cleaned_data['email'])
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'account/signup.html', {'form': form})


def checkout(request):
    form = AddressForm()
    data = cartData(request)

    items = data['items']
    order = data['order']

    cartItems = data['cartItems']
    context = {
        'title': 'Заказ',
        'form': form,
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, 'mainapp/checkout.html', context)


def addOrder(request):
    transaction_id = datetime.datetime.now().timestamp()

    data = cartData(request)
    items = data['items']

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        order.transaction_id = transaction_id

        if request.method == 'POST':
            form = AddressForm(request.POST)

            if form.is_valid():
                new = form.save(commit=False)
                new.customer = customer
                new.order = order
                new.save()
                order.save()
                for item in items:
                    product = Product.objects.get(id=item.product.id)
                    Cart.objects.create(product=product,
                                        order=order,
                                        quantity=item.quantity)
            items.delete()

    return redirect('order')


def contact(request):
    data = cartData(request)
    form = QuestionForm()
    cartItems = data['cartItems']

    context = {
        'title': 'Контакты',
        'cartItems': cartItems,
        'form': form,
    }
    return render(request, 'mainapp/contact.html', context)


def about(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {
        'title': 'Про нас',
        'cartItems': cartItems,
    }
    return render(request, 'mainapp/about.html', context)


def addQuestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    if action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Added', safe=False)


def order(request):
    return render(request, 'mainapp/order.html')
