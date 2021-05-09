from django.contrib import admin
from django.urls import path
from mysites import views
urlpatterns = [
    path('test/',views.test),
    path('login/', views.userlogin),
    path('logout/',views.user_logout),
    path('getstatus/',views.get_status),
    path('getinfo/',views.getinfo)
]