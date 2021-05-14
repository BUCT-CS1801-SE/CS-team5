from django.contrib import admin
from django.urls import path
from mysites import views
urlpatterns = [
    path('test/',views.test),
    path('login/', views.userlogin),
    path('logout/',views.user_logout),
    path('getstatus/',views.get_status),
    path('getinfo/',views.getinfo),
    path('addinfoTonews/',views.addinfoTonews),
    path('getnewsdata/',views.getnewsdata),
    path('deleteNewsOneitem/',views.deleteNewsOneitem),
    path('deleteExplainOneitem/',views.deleteExplainOneitem),
    path('getexplaindata/',views.getexplaindata),
    path('addinfoToexplain/',views.addinfoToexplain),
    path('deleteCommentOneitem/',views.deleteCommentOneitem),
    path('addinfoTocomment/',views.addinfoTocomment),
    path('getcommentdata/',views.getcommentdata)
]