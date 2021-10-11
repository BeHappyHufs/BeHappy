from django import urls
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<int:id>', views.detail, name='detail'),
    path('update/<int:boardid>/',views.update, name='update'),
    path('delete/<int:boardid>', views.delete, name='delete'),
    url('post/(?P<id>[0-9]+)$', views.detail, name='detail'),
    

] 