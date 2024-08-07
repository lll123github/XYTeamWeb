from .views import *
from django.urls import path


urlpatterns = [
    path('/page/login',PageLogin.as_view()),
    path('',Login.as_view(),)
]
