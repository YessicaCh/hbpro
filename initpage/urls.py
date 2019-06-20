# pages/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.InitPageView.as_view(), name='home'),
]