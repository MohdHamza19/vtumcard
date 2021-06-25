from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('sem3/', views.marks3, name="Sem3"),
    path('sem5/', views.marks5, name="Sem5"),
    path('select_sem/', views.selectSem, name="SelectSem"),
    path('download/<str:dd>', views.download, name="Download"),
    path('calc/', views.calc, name="Calculator"),
]
