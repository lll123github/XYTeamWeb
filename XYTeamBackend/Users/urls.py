from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path("",User.as_view(),name='User')
]