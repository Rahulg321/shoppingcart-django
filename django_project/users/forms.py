from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


#model form is a form that will allow us to work with a specific dataModel

class UserUpdateForm(forms.ModelForm):
    # default -> required == True
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserRegisterForm(UserCreationForm):
    # default -> required == True
    email = forms.EmailField()

    class Meta:
        # the model it interacts with
        model = User
        # the order in which the fields will be shown in the form
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

