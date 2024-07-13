from django import forms
from django.contrib.auth.models import User
from .models import UserInfo

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['phone', 'TMPID', 'TMPName', 'steamID', 'QQ', 'credit']