from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# since we didnt specify the route
# it posts our data back to this route
def register(request):
    # POST -> WHEN OUR FORM DATA IS SUBMITTED USING A SECURE SERVER
    # if we get a post request then a new form is created with that POST data
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        context = {
            'form': form
        }
        # validate the form
        # checks if our data is valid when submitted
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
# cleaned_data -> dictionary containing our form data

        # flashmessage-> onetime alerts to the data
            messages.success(request, f'Your account has been created, you can login to the main page {username}')

        # redirect to our selected page after successful form submition
            return redirect('login')

    else:
        # if it is a get request we will create an entirely new form
        form = UserRegisterForm()
        context = {
            'form': form
        }
    return render(request, 'users/register.html', context)


# user needs to be logged in order to access that view
@login_required
def profile(request):
    if request.method == 'POST':
    #populate the form with the existing data  
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    
    return render(request, 'users/profile.html', context)
