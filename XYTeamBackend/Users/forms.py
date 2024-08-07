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
        help_texts={
            'username':('必填；长度为150个字符或以下；只能包含汉字、字母、数字、特殊字符“@”、“.”、“-”和“_”。'),
            'email':('选填'),
            'password':('必填')
        }

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['phone', 'TMPID', 'TMPName', 'steamID', 'QQ']
        labels={
            'phone':('手机电话号码'),
            'TMPName':('TruckerMP用户名'),
            'QQ':('QQ号码'),
        }
        help_texts={
            'phone':('选填，需要为11位'),
            'TMPID':('必填'),
            'TMPName':('选填'),
            'steamID':('选填'),
            'QQ':('选填'),
        }
        error_messages={
            'phone':{
                'min_value':'输入的手机电话号码不合适',
                'max_value':'输入的手机电话号码不合适',
            },
            'TMPID':{
                'max_value':'输入的TMPID不合适',
            },
            'steamID':{
                'min_value':'输入的steamID不合适',
                'max_value':'输入的steamID不合适',
            }

        }

