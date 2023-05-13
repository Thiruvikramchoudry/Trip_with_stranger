"""Trip_with_Strangers URL Configuration

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
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('comments',views.comment,name="comments"),
    path('login', views.login, name='login'),
    path('register', views.register, name="register"),
    path('userpage',views.dynamic_page_notjoined,name="userpage"),
    path('createslot_phase1',views.create_slot_phase1,name="createslot_phase1"),
    path('logout',views.logout,name="logout"),
    path('joinuser/<slotid>',views.joinuser,name="joinuser"),
    path('slotpage/<str:slotid>',views.slotpage,name="slotpage"),
    path('delete_slot',views.delete_slot,name="delete_slot"),
    path('leave_slot',views.leave_slot,name="leave_slot"),
    path('sample',views.sample,name="sample"),
]

#{% url 'joinuser' slot.slotname %}
