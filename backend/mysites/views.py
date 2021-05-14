from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json
from mysites.models import newstable, explaintable, userComments
from django.forms.models import model_to_dict

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


#shenxiaowei's data operation:
def addinfoTonews(request):
    json_str = request.body
    dict_data = json.loads(json_str)
    newsdata = newstable()
    newsdata.newsID = dict_data.get('newsID')
    newsdata.museumID = dict_data.get('museumID')
    newsdata.newsTitle = dict_data.get('newsTitle')
    newsdata.newsTime = dict_data.get('newsTime')
    newsdata.newsmaintext = dict_data.get('newsmaintext')
    newsdata.attitude = dict_data.get('attitude')
    newsdata.status = dict_data.get('status')
    obj = newstable.objects.filter(newsID=newsdata.newsID)
    print(newsdata.newsID)
    if obj.count() == 1:
        obj.update(**dict_data)#大量更新
    else:
        newsdata.save()
    return JsonResponse({"status":0})

def getnewsdata(request):
    page = int(request.GET.get("page"))
    pageSize = int(request.GET.get("pageSize"))
    LpageNum = page*pageSize
    HpageNum = (page+1)*pageSize
    obj = newstable.objects.all()
    data=[]
    if obj.count()>=LpageNum and obj.count()<=HpageNum:
        List = obj.order_by('newsID')[LpageNum:HpageNum-1]
        for q in List:
            data.append(model_to_dict(q))
        return JsonResponse(data,safe=False)
        pass
    elif obj.count()>=LpageNum:
        List = obj.order_by('newsID')[LpageNum:]
        for q in List:
            data.append(model_to_dict(q))
        return JsonResponse(data, safe=False)
        pass
    else:
        return JsonResponse({"status": 1})

def deleteNewsOneitem(request):
    ID = int(request.GET.get('ID'))
    obj = newstable.objects.get(newsID=ID)
    obj.delete()
    return JsonResponse({"status":1})
    pass

def deleteExplainOneitem(request):
    ID = int(request.GET.get('ID'))
    obj = explaintable.objects.get(explanationID=ID)
    obj.delete()
    return JsonResponse({"status": 1})
    pass

def getexplaindata(request):
    page = int(request.GET.get("page"))
    pageSize = int(request.GET.get("pageSize"))
    LpageNum = page * pageSize
    HpageNum = (page + 1) * pageSize
    obj = explaintable.objects.all()
    data = []
    if obj.count() >= LpageNum and obj.count() <= HpageNum:
        List = obj.order_by('explanationID')[LpageNum:HpageNum - 1]
        for q in List:
            data.append(model_to_dict(q))
        return JsonResponse(data, safe=False)
        pass
    elif obj.count() >= LpageNum:
        List = obj.order_by('explanationID')[LpageNum:]
        for q in List:
            data.append(model_to_dict(q))
        return JsonResponse(data, safe=False)
        pass
    else:
        return JsonResponse({"status": 1})

def addinfoToexplain(request):
    json_str = request.body
    dict_data = json.loads(json_str)
    newsdata = explaintable()
    newsdata.explanationID = dict_data.get('explanationID')
    newsdata.explanationName = dict_data.get('explanationName')
    newsdata.explainerID = dict_data.get('explainerID')
    newsdata.explanationTime = dict_data.get('explanationTime')
    newsdata.explanationLanguage = dict_data.get('explanationLanguage')
    newsdata.recommendedTime = dict_data.get('recommendedTime')
    newsdata.status = dict_data.get('status')
    obj = explaintable.objects.filter(explanationID=newsdata.explanationID)
    print(newsdata.explanationID)
    if obj.count() == 1:
        obj.update(**dict_data)  # 大量更新
    else:
        newsdata.save()
    return JsonResponse({"status": 0})

def deleteCommentOneitem(request):
    ID = int(request.GET.get('ID'))
    obj = userComments.objects.get(commentID=ID)
    obj.delete()
    return JsonResponse({"status": 1})
    pass

def addinfoTocomment(request):
    json_str = request.body
    dict_data = json.loads(json_str)
    newsdata = userComments()
    newsdata.commentID = dict_data.get('commentID')
    newsdata.userID = dict_data.get('userID')
    newsdata.museumID = dict_data.get('museumID')
    newsdata.comment = dict_data.get('comment')
    newsdata.sentiAnalysis_environment = dict_data.get('sentiAnalysis_environment')
    newsdata.sentiAnalysis_exhibit = dict_data.get('sentiAnalysis_exhibit')
    newsdata.sentiAnalysis_service = dict_data.get('sentiAnalysis_service')
    newsdata.commentdata = dict_data.get('commentdata')
    newsdata.status = dict_data.get('status')
    obj = userComments.objects.filter(commentID=newsdata.commentID)
    print(newsdata.commentID)
    if obj.count() == 1:
        obj.update(**dict_data)  # 大量更新
    else:
        newsdata.save()
    return JsonResponse({"status": 0})

def getcommentdata(request):
    page = int(request.GET.get("page"))
    pageSize = int(request.GET.get("pageSize"))
    LpageNum = page * pageSize
    HpageNum = (page + 1) * pageSize
    obj = userComments.objects.all()
    data = []
    if obj.count() >= LpageNum and obj.count() <= HpageNum:
        List = obj.order_by('commentID')[LpageNum:HpageNum - 1]
        for q in List:
            data.append(model_to_dict(q))
        return JsonResponse(data, safe=False)
        pass
    elif obj.count() >= LpageNum:
        List = obj.order_by('commentID')[LpageNum:]
        for q in List:
            data.append(model_to_dict(q))
        return JsonResponse(data, safe=False)
        pass
    else:
        return JsonResponse({"status": 1})