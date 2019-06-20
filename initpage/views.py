from django.shortcuts import render
# Create your views here.
# pages/views.py
from django.views.generic import TemplateView


class InitPageView(TemplateView):
    template_name = 'initpage/index.html'