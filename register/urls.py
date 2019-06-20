from django.conf.urls import url

from register.views import register_db,SignUp
#url(r'^',register_db, name='register'), 

urlpatterns = [
    url('', register_db,name='register'), 

]
