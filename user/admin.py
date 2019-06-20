from django.contrib import admin

# Register your models here.
# users/admin.py
#from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import CustomUser
from .models import HbproUser

"""class CustomUserAdmin(UserAdmin):
    model = HbproUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm"""
admin.site.register(HbproUser)

"""admin.site.register(HbproUser, CustomUserAdmin)
admin.site.register(Student2)
admin.site.register(Mentor)
admin.site.register(Program)
admin.site.register(Students_Mentor)
admin.site.register(Course)
admin.site.register(Courses_Student)"""