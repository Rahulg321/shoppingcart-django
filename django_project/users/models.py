from django.db import models
# importing our user model
from django.contrib.auth.models import User
# extending the functionality of our user Model


class Profile(models.Model):
    # if user deleted -> delete profile
    # if profile deleted -> dont delete user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
