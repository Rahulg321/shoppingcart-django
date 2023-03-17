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
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

# lets us access this as an attribute
# fixing the issue if there is no image then what to display
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url


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


# ORDER -> CART FOR A SINGLE USER
class Order(models.Model):
    """
        An order can be made by multiple customers
    """
    # IF A CUSTOMER GETS DELETED WE DONT WANT TO DELETE THE ORDER, WE JUST WANT TO SET THE CUTSOMER VALUE TO NULL
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    # whether the order is complete and we are ready for the checkout
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        # gets all orderitems from the child database
        orderitems = self.orderitem_set.all()
# gets the total for each individual items and then sums them all up for the cart total
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        # how many different products are there in our cart
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


"""
Items that need to be added to our order with the many to one relationship
"""


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
