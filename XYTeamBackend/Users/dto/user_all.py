from ..models import *
from django.contrib.auth.models import User

def user_all(user: User):
    userinfo=user.userinfo
    response={'id':user.id,'username':user.username,'email':user.email,'phone':userinfo.phone,'TMPID':userinfo.TMPID,'TMPName':userinfo.TMPName,'steamID':userinfo.steamID,'QQ':userinfo.QQ,'credit':userinfo.credit}
    return response