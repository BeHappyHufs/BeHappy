from django import urls
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #게시판
    path('main', views.main, name='main'),
    path('post', views.post, name='post'),
    path('post/<int:id>', views.detail, name='detail'),
    path('update/<int:boardid>/',views.update, name='update'),
    path('delete/<int:boardid>', views.delete, name='delete'),
    url('post/(?P<id>[0-9]+)$', views.detail, name='detail'),
    
    #로그인
    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
   
] 