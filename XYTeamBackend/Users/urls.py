from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('/page/create',PageCreateUser.as_view()),
    path('',UsersActions.as_view()),
    path('/<int:TMPID>',OneUserActions.as_view()),
    
    
]