from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_task/', views.add_task, name="add_task"),
    path('complete/', views.complete, name="complete"),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    # path('register/', views.registerPage, name="register"),


]
