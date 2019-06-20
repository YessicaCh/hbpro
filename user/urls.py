# users/urls.py
from django.urls import path,include
from . import views

import pudb; pudb.set_trace()

urlpatterns = [
	path('', views.SignUp.as_view(), name='signup'),
	#path('', include('initpage.urls')),
    #path('register/', views.SignUp.as_view(), name='signup'),
    #path('users/login/', include('initpage.urls')), # new
]