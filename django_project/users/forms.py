from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # default -> required == True
    email = forms.EmailField()

    class Meta:
        # the model it interacts with
        model = User
        # the order in which the fields will be shown in the form
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
