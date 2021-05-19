from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models
import json
from mysites.models import newstable, explaintable, userComments
from django.forms.models import model_to_dict
from .models import UploadExplanation
from django.http import HttpResponse
import os
# Create your views here.
def test(request):
    db = request.GET
    return JsonResponse({"status":0,"message":"This is a message","mydata":db})
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

def manage_delete(request):
    db = request.GET.get("data")
    msg = User.objects.filter(pk=db).delete()
    return JsonResponse({"status": 0,"data":msg})

def register(request):
    if request.method == "POST":
        data = json.loads(request.body)

        if request.GET.get("select") is not None:
            select_username = data.get("select_username")
            print(select_username)
            try:
                User.objects.get(username=select_username)
                return JsonResponse({
                    "status": 0,
                    "is_indb": 1
                })
            except:
                return JsonResponse({
                    'status': 0,
                    "is_indb": 0
                })
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        if username is not None and password is not None and email is not None:
            try:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                login_user = authenticate(request, username=username, password=password)
                if login_user:
                    return JsonResponse({
                        "status": 0,
                        "message": "Register Success"
                    })

            except:
                return JsonResponse({
                    "status": 2,
                    "message": "注册失败, 该用户名已经存在."
                })

    else:
        return JsonResponse({
            "status": 1,
            "message": "error method"
        })

def m_change(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("username")
        paword = data.get("password")
        em = data.get("email")
        userid = data.get("id")
        info = User.objects.filter(pk=userid).update(username = name,password = paword,email = em)
        return JsonResponse({
            "status": 0,
            "message": "Success",
            "info":info
        })
    else:
        return JsonResponse({
            "status": 1,
            "message": "error method"
        })


def getmuseum(request):
    db = models.museum.objects.all()
    data = [
        {
            "id": i.mu_id,
            "name": i.mu_name,
            "location": i.mu_location,
            "intro": i.mu_intro,
            "open": i.mu_open,
            "link": i.mu_link,
            "level": i.mu_level,
            "tele": i.mu_tele,
            "grade": i.mu_grade,
            "fee": i.mu_fee,
            "bulid": i.mu_bulid,
            "num": i.mu_num,
            "city": i.mu_look,
            "status": i.mu_status,
            "look": i.mu_look

        }
        for i in db]
    print(data)
    return JsonResponse({"status": 0, "data": data})


def getcollection(request):
    db = models.collection.objects.all()
    data = [
        {
            "id": i.co_id,
            "name": i.co_name,
            "mu_id": i.mu_id,
            "intro": i.co_intro,
            "image": i.co_image,
            "age": i.co_age,
            "status": i.co_status
        }
        for i in db]
    return JsonResponse({"status": 0, "data": data})


def getexhibition(request):
    db = models.exhibition.objects.all()
    data = [
        {
            "id": i.ex_id,
            "mu_id": i.mu_id,
            "location": i.ex_location,
            "time": i.ex_time,
            "theme": i.ex_theme,
            "intro": i.ex_intro,
            "tele": i.ex_tele,
            "list": i.ex_list,
            "pic": i.ex_pic,
            "status": i.ex_status
        }
        for i in db]
    return JsonResponse({"status": 0, "data": data})


def add_museum(request):
    data = json.loads(request.body)
    name = data.get("name")
    location = data.get("location")
    intro = data.get("intro")
    open = data.get("open")
    link = data.get("link")
    level = data.get("level")
    grade = data.get("grade")
    fee = data.get("fee")
    tele = data.get("tele")
    bulid = data.get("bulid")
    num = data.get("num")
    city = data.get("city")
    status = data.get("status")
    look = data.get("look")
    models.museum.objects.create(mu_tele=tele, mu_name=name, mu_location=location, mu_intro=intro, mu_open=open,
                                 mu_link=link, mu_level=level, mu_grade=grade, mu_fee=fee, mu_look=look, mu_bulid=bulid,
                                 mu_num=num, mu_city=city, mu_status=status)


def edit_museum(request):
    data = json.loads(request.body)
    i = data.get("id")
    name = data.get("name")
    location = data.get("location")
    intro = data.get("intro")
    open = data.get("open")
    link = data.get("link")
    level = data.get("level")
    grade = data.get("grade")
    tele = data.get("tele")
    fee = data.get("fee")
    bulid = data.get("bulid")
    num = data.get("num")
    city = data.get("city")
    status = data.get("status")
    look = data.get("look")
    models.museum.objects.filter(mu_id=i).update(mu_tele=tele, mu_name=name, mu_location=location, mu_intro=intro,
                                                 mu_open=open, mu_link=link, mu_level=level, mu_grade=grade, mu_fee=fee,
                                                 mu_look=look, mu_bulid=bulid, mu_num=num, mu_city=city,
                                                 mu_status=status)


def delete_museum(request):
    data = json.loads(request.body)
    i = data.get("id")
    models.museum.objects.filter(mu_id=i).delete()
    return JsonResponse({"status": 0, "data": data})


def add_collection(request):
    data = json.loads(request.body)
    name = data.get("name")
    mu_id = data.get("mu_id")
    intro = data.get("intro")
    status = data.get("status")
    image = data.get("image")
    age = data.get("age")
    models.collection.objects.create(co_name=name, mu_id=mu_id, co_intro=intro, co_status=status, co_image=image,
                                     co_age=age)


def edit_collection(request):
    data = json.loads(request.body)
    i = data.get("id")
    name = data.get("name")
    mu_id = data.get("mu_id")
    intro = data.get("intro")
    status = data.get("status")
    image = data.get("image")
    age = data.get("age")
    models.collection.objects.filter(co_id=i).update(co_name=name, mu_id=mu_id, co_intro=intro, co_statsu=status,
                                                     co_image=image, co_age=age)


def delete_collection(request):
    data = json.loads(request.body)
    i = data.get("id")
    models.collection.objects.filter(co_id=i).delete()
    return JsonResponse({"status": 0, "data": data})


def add_exhibition(request):
    data = json.loads(request.body)
    mu_id = data.get("mu_id")
    location = data.get("location")
    intro = data.get("intro")
    time = data.get("time")
    tele = data.get("tele")
    theme = data.get("theme")
    list = data.get("list")
    status = data.get("status")
    pic = data.get("pic")
    models.exhibition.objects.create(ex_tele=tele, ex_location=location, mu_id=mu_id, ex_intro=intro, ex_time=time,
                                     ex_theme=theme, ex_list=list, ex_pic=pic, ex_status=status)


def edit_exhibition(request):
    data = json.loads(request.body)
    i = data.get("id")
    mu_id = data.get("mu_id")
    location = data.get("location")
    intro = data.get("intro")
    time = data.get("time")
    tele = data.get("tele")
    theme = data.get("theme")
    list = data.get("list")
    status = data.get("status")
    pic = data.get("pic")
    models.exhibition.objects.filter(ex_id=i).update(ex_tele=tele, ex_location=location, mu_id=mu_id, ex_intro=intro,
                                                     ex_time=time, ex_theme=theme, ex_list=list, ex_pic=pic,
                                                     ex_status=status)


def delete_exhibition(request):
    data = json.loads(request.body)
    i = data.get("id")
    models.exhibition.objects.filter(ex_id=i).delete()
    return JsonResponse({"status": 0, "data": data})

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

def getuserinfo(request):
    data = models.userInfo.objects.all()
    data = [
        {
            "userID": i.userID,
            "username": i.username,
            "nickname": i.nickname,
            "telephone": i.telephone,
            "idcard": i.idcard,
            "password": i.password,
            "userRole": i.userRole,
            "userCreateDate":i.userCreateDate
        }
        for i in data]
    return JsonResponse({"status": 0, "data": data})

def userdelete(request):
    db = request.GET.get("data")
    msg = models.userInfo.objects.filter(pk=db).delete()
    return JsonResponse({"status": 0, "data": msg})

def useradd(request):
    data = json.loads(request.body)
    username = data.get("username")
    nickname = data.get("nickname")
    telephone = data.get("telephone")
    idcard = data.get("idcard")
    password = data.get("password")
    userRole = data.get("userRole")
    models.userInfo.objects.create(username=username,nickname=nickname,telephone=telephone,idcard=idcard,password=password,userRole=userRole)
    return JsonResponse({"status":0,"msg":data})

def useredit(request):
    data = json.loads(request.body)
    userID = data.get("userID")
    username = data.get("username")
    nickname = data.get("nickname")
    telephone = data.get("telephone")
    idcard = data.get("idcard")
    password = data.get("password")
    userRole = data.get("userRole")
    msg = models.userInfo.objects.filter(pk=userID).update(
        userID=userID,username=username,nickname=nickname,telephone=telephone,idcard=idcard,password=password,userRole=userRole
    )
    return JsonResponse({"status":0,"msg":msg})

def backup(request):
    data = json.loads(request.body)
    flag = data.get("flag")
    if flag==1:
        db = "python manage.py dumpdata --format=json > bak.json"
        d = os.popen(db)
        f = d.read()
        return JsonResponse({"status":0,"msg":f})
    else:
        return JsonResponse({"status":1})

def recovery(request):
    data = json.loads(request.body)
    flag = data.get("flag")
    if flag==1:
        db = "python manage.py loaddata bak.json"
        d = os.popen(db)
        f = d.read()
        return JsonResponse({"status":0,"msg":f})
    else:
        return JsonResponse({"status":1})


def ret_user(request):
    if request.method == "GET":
        upName=[]
        db = UploadExplanation.objects.all()
        for item in db:
            if item.visible==True:
                upName.append(item.name)
        # upName = [i.name for i in db]
        return JsonResponse({"status":0,"name":upName})
    else:
        return JsonResponse(json.dumps({"status":0,"message":"you need GET method"}, ensure_ascii=False))

def ret_audio(request,num):
    if request.method == "GET":
        db = UploadExplanation.objects.all()
        upAudio = []
        for item in db:
            upAudio.append(item.audio)
        print(upAudio[num])
        return HttpResponse(upAudio[num])
    else:
        return JsonResponse(json.dumps({"status":0,"message":"you need GET method"}, ensure_ascii=False))

def delete_data(request):
    if request.method == 'POST':
        name = json.loads(request.body)
        tmp=name['del']
        print(tmp)
        get_db=UploadExplanation.objects.filter(name=tmp)
        get_db.update(visible=False)
    return JsonResponse({"success":"success post"})

def modify_data(request):
    if request.method == 'POST':
        name = json.loads(request.body)
        tmp=name['modify']
        print(tmp)
        get_db=UploadExplanation.objects.filter(name=tmp)
        get_db.update(name='need modify',visible=False)
    return JsonResponse({"success":"success modify"})
