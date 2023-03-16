from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# the user that was automatically created when we ran the migrate command before hand


class Customer(models.Model):
    # if the user is deleted, delete the model itself
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # will automatically use the current datetime while creating a post
    date_posted = models.DateTimeField(default=timezone.now)
    # ONE TO MANY RELATION B/W USER AND POSTS
    # IF A USER IS DELETED, THEIR ALL OF THEIR POSTS AS WELL
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    # IF A CUSTOMER GETS DELETED WE DONT WANT TO DELETE THE ORDER, WE JUST WANT TO SET THE CUTSOMER VALUE TO NULL
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
