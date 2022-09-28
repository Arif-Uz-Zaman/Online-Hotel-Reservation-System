from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from home import views




urlpatterns = [
    path('',views.index,name="index"),
    path('home.html',views.home,name="home"),
    path('About_us/',views.aboutus,name="AboutUs"),
    path('home2.html',views.home2,name="home2"),
]
