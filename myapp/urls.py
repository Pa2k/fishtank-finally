from django.urls import path,include
from .views import *
urlpatterns = [
    path("",index,name="index"),
    path("accounts/",include('django.contrib.auth.urls')),
    path("accounts/register/",registration_view,name="register")
]
