from django import urls
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #게시판
    path('main/', views.main, name='main'),
    path('write/', views.write, name='write'),
    path('detail/<int:boardid>/', views.detail, name='detail'),
    path('delete/<int:boardid>', views.delete, name='delete'),
    path('update/<int:boardid>/', views.update, name='update'),
    url('post/(?P<id>[0-9]+)$', views.detail, name='detail'),

    #로그인
    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    path('logout/', views.logout, name='logout'),

    # 메인 화면
    path('',views.showMain),

] 