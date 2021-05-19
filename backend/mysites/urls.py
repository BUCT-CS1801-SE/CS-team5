from django.contrib import admin
from django.urls import path
from mysites import views
urlpatterns = [
    path('test',views.test),
    path('login/', views.userlogin),
    path('logout/',views.user_logout),
    path('getstatus/',views.get_status),
    path('getinfo/',views.getinfo),
    path('m_d',views.manage_delete),
    path('register', views.register),
    path('m_change',views.m_change),

    path('addmuseum',views.add_museum),
    path('deletemuseum',views.delete_museum),
    path('editmuseum',views.edit_museum),
    path('getmuseum/',views.getmuseum),

    path('addcollection',views.add_collection),
    path('deletecollection',views.delete_collection),
    path('editcollection',views.edit_collection),
    path('getcollection/',views.getcollection),

    path('addexhibition',views.add_exhibition),
    path('getexhibition/',views.getexhibition),
    path('deleteexhibition',views.delete_exhibition),
    path('editexhibition',views.edit_exhibition),

    path('addinfoTonews/',views.addinfoTonews),
    path('getnewsdata/',views.getnewsdata),
    path('deleteNewsOneitem/',views.deleteNewsOneitem),
    path('deleteExplainOneitem/',views.deleteExplainOneitem),
    path('getexplaindata/',views.getexplaindata),
    path('addinfoToexplain/',views.addinfoToexplain),
    path('deleteCommentOneitem/',views.deleteCommentOneitem),
    path('addinfoTocomment/',views.addinfoTocomment),
    path('getcommentdata/',views.getcommentdata),

    path('getuserinfo/',views.getuserinfo),
    path('u_d',views.userdelete),
    path('useradd',views.useradd),
    path('u_change',views.useredit),

    path('backup',views.backup),
    path('recovery',views.recovery),

    path('user/',views.ret_user),
    path('audio/<int:num>',views.ret_audio),
    path('del/',views.delete_data),
    path('modify/',views.modify_data)
]