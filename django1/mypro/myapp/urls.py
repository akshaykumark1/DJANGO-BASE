
from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index1',views.index1,name='index1'),
    path('index2',views.index2,name='index2'),
    path('index3',views.index3,name='index3'),
    

]
