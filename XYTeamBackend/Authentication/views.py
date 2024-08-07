from django.shortcuts import render
from django.views import View
import demjson
from .forms import LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from utils.token import *

# Create your views here.

class Login(View):
    def post(self,request,TMPID):
        login_form=LoginUserForm(request.POST)
        if not login_form.is_valid():
            pass #错误登录请求
        body=demjson.decode(request.body)
        if not body['username']:
            if not body['email']:
                pass#错误登录请求
            user=User.objects.filter(email=login_form.cleaned_data['email'])
            user=user[0]
            if not user:
                pass#错误登录请求
            username=user.username
        else:
            username=login_form.cleaned_data['username']
        password=login_form.cleaned_data['password']
        user=authenticate(username,password)
        if user is not None:
            token=generate_token(user)
        else:
            pass#错误登录请求

class PageLogin(View):
    template_name='PageLogin.html'
    def get(self,request,*args, **kwargs):
        login_form=LoginUserForm()
        return render(request,self.template_name,{'login_form':login_form})






        

