from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from User import views




urlpatterns = [

    path('editinfo',views.editinfo,name="editinfo"),
    path('editinfo.html',views.editinfo,name="editinfo1"),
    path('profile',views.userProfile,name="profile"),
    path('profile.html',views.userProfile,name="profile1"),


]
