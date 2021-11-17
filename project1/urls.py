"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http import response
from django.urls import path
from company import views
from user.views import  login, logout

from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/',views.index,name="company"),
    # url(r'^insert/(?P<p_number>[0-9]+)/(?P<title>[a-zA-Z0-9_]+)$',views.insert),
    # url(r'^delete/(?P<p_number>[0-9]+)$',views.delete, ),
    # url(r'^update/(?P<p_number>[0-9]+)/(?P<title>[a-zA-Z0-9_]+)$',views.update)
    path('insert/',views.insert ,name="insert"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/',views.update,name="update"),
    path('listall',views.listall.as_view()),
    # url(r'^delete/(?P<p_number>[0-9]+)$',views.delete ,name="delete"),
    path('',login,name="login" ),
    path('logout',logout,name="logout" ),
    
]
