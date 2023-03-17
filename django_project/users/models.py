from django.db import models
from PIL import Image
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

#the method that gets run after our model is saved 
    def save(self):
#run the save method of our parent class
        super().save()
  #open the img of our current instance      
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            
            img.thumbnail(output_size)
            img.save(self.image.path)
        
        