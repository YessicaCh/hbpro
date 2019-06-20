from django.conf.urls import url

from contentuser.views import index, imdexTeam

urlpatterns = [
    url(r'^progress',index),
    url(r'^team', imdexTeam),
]
