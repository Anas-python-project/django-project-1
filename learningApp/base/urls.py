from django.urls import path
from . import views

urlpatterns = [
    path('<str:userName>/', views.home, name="home"),
    path('complete/<str:userName>/', views.complete, name="complete"),
]
