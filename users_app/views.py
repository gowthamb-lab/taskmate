from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomRegistrationForm
#from django.http import HttpResponse
# Create your views here.
#from django.contrib.auth.forms import UserCreationForm


def register(request):
    #context = {'register_text': 'Welcome from Jinja2 template to register page'}
    #return render(request, 'register.html', context)    
    if request.method == 'POST':
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ('New User Registered!'))
            return redirect('register')
    else:

        register_form = CustomRegistrationForm()
    return render(request, 'register.html', {'register_form': register_form})
    #return HttpResponse("This is the User Registration view")