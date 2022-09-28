from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from account import views
import account


urlpatterns = [
    path('registration',views.Registration,name="registrtion"),
    path('registration.html',views.Registration,name="registrtion1"),
    path('login/',views.userlogin,name="login"),
    path('login.html',views.userlogin,name="login1"),
    path('logout/', views.userlogout, name='logout'),
    # path('login/',auth_views.LoginView.as_view(template_name="login/login.html"),name="login"),
    # path('loginout/',auth_views.LogoutView.as_view(template_name="index.html"),name="login"),
    

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="forget/forget.html"),name="reset_password"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="forget/resetsent.html"),name="reset_password_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="forget/resertform.html"),name="reset_password_Confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="reset_password_Complete"),
    ]