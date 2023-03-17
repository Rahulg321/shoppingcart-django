from django.shortcuts import render
from .models import *
from django.http import JsonResponse


# context -> pass additional info in our template
def home(request):
    products = Product.objects.all()
    context = {"products": products}

    # looks for subdir within our templates
    return render(request, 'blog/home.html', context)


def review(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/review.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer

# creating a new object if it doesnt exist or quering one
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
# returns all of the order items that has this specific order
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'blog/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}

    return render(request, 'blog/checkout.html', context)


def updateItem(request):
    return JsonResponse("item was added", safe=False)
