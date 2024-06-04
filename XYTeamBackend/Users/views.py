from django.http import JsonResponse
import demjson
from django.contrib.auth.models import User
from .models import *
from django.views import View
# Create your views here.
class UserActions(View):
    def get(self, request):#查
        body=demjson.decode(request.body)
        users=User.objects.all()
        if 'id' in body:
            user=users.filter(id=body['id'])
            if not user.exists():
                return JsonResponse({'msg':"User is not found when finding id!"},status=404)
            user=user[0]
            userinfo=user.userinfo
            return JsonResponse(data={'id':user.id,'username':user.username,'phone':userinfo.phone,'TMPID':userinfo.TMPID,'TMPName':userinfo.TMPName,'steamID':userinfo.steamID,'QQ':userinfo.QQ},status=200)
        
        if 'username' in body:
            users=users.filter(username=body['username'])
            if not users.exists():
                return JsonResponse({'msg':"Users is not found when finding username!"},status=404)
        if 'email' in body:
            users=users.filter(email=body['email'])
            if not users.exists():
                return JsonResponse({'msg':"Users is not found when finding email!"},status=404)
        # print(users)
        # users=users[0]
        # print(users)
        # usersinfo=users.userinfo
        # print()
        # if not usersinfo.exists():
        #     return JsonResponse({'msg':"UsersInfo is not found!"},status=404)
        if 'phone' in body:
            users=users.filter(userinfo__phont=body['phone'])
            if not users.exists():
                return JsonResponse({'msg':"UsersInfo is not found when finding phone!"},status=404)
        if 'TMPID' in body:
            users=users.filter(userinfo__TMPID=body['TMPID'])
            if not users.exists():
                return JsonResponse({'msg':"UsersInfo is not found when finding TMPID!"},status=404)
        if 'TMPName' in body:
            users=users.filter(userinfo__TMPName=body['TMPName'])
            if not users.exists():
                return JsonResponse({'msg':"UsersInfo is not found when finding TMPName!"},status=404)
        if 'steamID' in body:
            users=users.filter(userinfo__steamID=body['steamID'])
            if not users.exists():
                return JsonResponse({'msg':"UsersInfo is not found when finding steamID!"},status=404)
        if 'QQ' in body:
            users=users.filter(userinfo__QQ=body['QQ'])
            if not users.exists():
                return JsonResponse({'msg':"UsersInfo is not found when finding QQ!"},status=404)
        print(users)
        results_list=[]
        for user in users:#还需要对多个查询结果和单个查询结果的结果进行区分
            print(user)
            userinfo=UserInfo.objects.filter(user=user)
            userinfo=userinfo[0]
            results_list.append({'id':user.id,'username':user.username,'phone':userinfo.phone,'TMPID':userinfo.TMPID,'TMPName':userinfo.TMPName,'steamID':userinfo.steamID,'QQ':userinfo.QQ})
        return JsonResponse({"userinfo":results_list},status=200)

    def post(self, request):#增
        body=demjson.decode(request.body)
        user=User.objects.create_user(username=body['username'],password=body['password'])
        user_info=UserInfo.objects.create(user=user,TMPID=body['TMPID'])
        if 'phone' in body:
            user_info.phone=body['phone']
        if 'TMPName' in body:
            user_info.TMPName=body['TMPName']
        if 'steamID' in body:
            user_info.steamID=body['steamID']
        if 'QQ' in body:
            user_info.QQ=body['QQ']
        user_info.save()
        return JsonResponse({'id':user.id},status=200)



    def put(self, request,TMPID):#改
        body=demjson.decode(request.body)
        userinfo=UserInfo.objects.filter(TMPID=TMPID)
        if not userinfo.exists(): 
            return JsonResponse({'msg':"UserInfo is not found!"},status=404)
        userinfo=userinfo[0]
        user=userinfo.user
        print(user)
        # 暂时不支持修改TMPID
        # if 'TMPID' in body:
        #     print("Searching for the TMPID") 
        #     other_user_info=UserInfo.objects.filter(TMPID=body['TMPID'])
        #     if other_user_info.exists():
        #         return JsonResponse('User with this TMPID has existed!',status=400)
        #     userinfo.TMPID=body['TMPID']
        if 'username' in body:
            user.username=body['username']
        if 'email' in body:
            user.email=body['email']
        if 'password' in body:
            user.set_password(body['password'])
        if 'phone' in body:
            userinfo.phone=body['phone']
        if 'TMPName' in body:
            userinfo.TMPName=body['TMPName']
        if 'steamID' in body:
            userinfo.steamID=body['steamID']
        if 'QQ' in body:
            userinfo.QQ=body['QQ']
        # user.save()
        userinfo.save()
        return JsonResponse({'id':user.id},status=200)


    def delete(self, request, TMPID):#删
        userinfo=UserInfo.objects.filter(TMPID=TMPID)
        if not userinfo.exists():
            return JsonResponse({'msg':"UserInfo is not found!"},status=404)
        userinfo.delete()
        return JsonResponse({'msg':"UserInfo is deleted!"},status=200)

    

