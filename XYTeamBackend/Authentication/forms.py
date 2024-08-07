from django import forms
from django.contrib.auth.models import User
class LoginUserForm(forms.ModelForm):
    username=forms.CharField(required=False)
    email=forms.EmailField(required=False)
    class Meta:
        model =User
        fields = ['username','email','password']
        widgets={
            'password':forms.PasswordInput()
        }
        help_texts={
            'username':'您在本网站注册使用的用户名',
        }

