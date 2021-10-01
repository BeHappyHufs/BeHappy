

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from FindLocation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.showMap),
    path('show/',views.index),
    path('bin/',views.whereBin),
    path('seperate/',views.showDiffer),
]