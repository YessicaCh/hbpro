from django import forms
from user.models import HbproUser 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import HbproUser

#class CustomUserCreationForm(UserCreationForm):

#    class Meta(UserCreationForm):
#        model = HbproUser
#        fields = ('username', 'email')
class studentForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = HbproUser
		fields = ['name', 'last_name', 'nick_name',
                 'age', 'e_mail', 'number_phone', 'github','password1','password2']	
		widgets = {
		    'name': forms.TextInput(attrs={'placeholder': 'Name'}),
			'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
			'nick_name': forms.TextInput(attrs={'placeholder': 'Nickname'}),
			'age': forms.NumberInput(attrs={'placeholder': 'Age', 'min': 18}),
			'e_mail': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
			'number_phone': forms.NumberInput(attrs={'placeholder': 'Phone'}),
           	'github': forms.URLInput(attrs={'placeholder': 'Github'}),
           	'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
           	'password2': forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}),
        }