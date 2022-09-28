"""OHRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("OHRS_App.urls")),
    path('', include("account.urls")),
    path('', include("User.urls")),
    path('', include("home.urls")),
    path('', include("hotel.urls")),
    path('', include('django.contrib.auth.urls'))
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'OHRS Administration'           # default: "Django Administration"
admin.site.index_title = 'Hotel Data Base'                 # default: "Site administration"
admin.site.site_title = 'Adminsitration' # default: "Django site admin"
admin.site.site_url = 'http://127.0.0.1:8000/home2.html'