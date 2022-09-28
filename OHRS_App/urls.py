from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index1"),
    path("contactus.html", views.contactUs, name="contact"),
    path("message.html", views.cust_message, name="message"),

]