# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import HbproUser

class CustomUserCreationForm(UserCreationForm):
    #username = forms.TextInput(max_length=30, required=False, help_text='Optional.',attrs={'placeholder': 'Name'})
    #password = forms.PasswordInput(max_length=30, required=False, help_text='Optional.',attrs={'placeholder': 'Password'})
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta(UserCreationForm):
        model = HbproUser
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        } 
        fields = ('username','password')
        subject = forms.CharField(max_length=100, help_text='100 characters max.')
"""class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = HbproUser
        fields = ('username', 'email')
        widgets = {
           # telling Django your password field in the mode is a password input on the template
		    'username': forms.TextInput(attrs={'placeholder': 'Name'}),
        	'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }"""

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = HbproUser
        fields = UserChangeForm.Meta.fields