from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    
    path('',UserActions.as_view()),
    path('<int:TMPID>',UserActions.as_view()),
    
]