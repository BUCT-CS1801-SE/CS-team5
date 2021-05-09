from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json
# Create your views here.
def test(request):
    return JsonResponse({"status":0,"message":"This is a message"})
def get_status(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "status": 0,
            "username": str(request.user),
            "email": str(request.user.email),
        })
    else:
        return JsonResponse({
            "status": 1
        })
def user_logout(request):
    return JsonResponse({"status":0,"message":"logout success"})
def userlogin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        print(username)
        print(password)
        if username is not None and password is not None:
            islogin = authenticate(request, username=username, password=password)
            if islogin:
                login(request, islogin)
                print(request.session)
                return JsonResponse({
                    "status": 0,
                    "message": "Login Success",
                    "username": username
                })
            else:
                return JsonResponse({
                    "status": 1,
                    "message": "登录失败, 请检查用户名或者密码是否输入正确."
                })
        else:
            return JsonResponse({
                "status": 2,
                "message": "参数错误"
            })
def getinfo(request):
    db = User.objects.all()
    data = [
        {
            "id":i.id,
            "username": i.username,
            "password": i.password,
            "email":i.email
        }
        for i in db]
    return JsonResponse({"status":0,"data":data})