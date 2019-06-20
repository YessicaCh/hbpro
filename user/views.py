from django.shortcuts import render

# Create your views here.
# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('')
    template_name = 'register/index.html'
    import pudb; pudb.set_trace()
     widgets = {
           # telling Django your password field in the mode is a password input on the template
		    'username': forms.TextInput(attrs={'placeholder': 'Name'}),
        	'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

class HomePage(generic.CreateView):
    template_name = 'initpage/index.html'