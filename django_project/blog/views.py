from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView)


# classbasedviews list/delete/create


# context -> pass additional info in our template
def home(request):
    products = Product.objects.all()
    context = {"products": products}

    # looks for subdir within our templates
    return render(request, 'blog/home.html', context)


def review(request):
    # list view ->  since our home page is listing our all of our blogs
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/review.html', context)


class PostListView(ListView):
    # model to interact with
    model = Post

    template_name = 'blog/review.html'
    context_object_name = 'posts'

    ordering = ['-date_posted']


class PostDetailView(DetailView):
    # model to interact with
    model = Post


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
    """_summary_

    Returns:
        this function updates the database for order and orderitems
        takes in a string of data from cart.js and get the product id and action associated with it
        from the product id, it gets the associcated product

        then gets the associcated order items based on the order and product id's
    """

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('ACTION:- ', action)
    print('productId:- ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("item was added", safe=False)
