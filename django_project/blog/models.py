from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#the user that was automatically created when we ran the migrate command before hand


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #will automatically use the current datetime while creating a post
    date_posted = models.DateTimeField(default = timezone.now)
    #ONE TO MANY RELATION B/W USER AND POSTS
    #IF A USER IS DELETED, THEIR ALL OF THEIR POSTS AS WELL
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.title
