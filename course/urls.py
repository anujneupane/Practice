from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('course/', views.studentInfo),
    path('aa/', views.showformdata),
    path('aaa/', views.showformloop),
    path('gg/', views.done)
    
]
