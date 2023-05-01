# from urllib import request

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskFrom
from django.db.models import Q # for using or, and operations with db 
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def loginPage(req):
      if req.method == 'POST':
         username = req.POST.get('username')
         password = req.POST.get('password')
         try:
            user = User.objects.get(username= username)
         except:
            messages.error(req, "User Does not Exist")
         user = authenticate(req, username=username,password=password)
         if user is not None:
            login(req,user)
            return redirect('home')
         else:
           
            messages.error(req, "username or password does not exist")

      context = {}
      return render(req,'base/user_form.html',context)
def logoutUser(req):
   logout(req)
   return redirect('home')

def home(req):
    tasks = Task.objects.filter(user_id=2)
    if req.method =='POST':
        form = TaskFrom(req.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')

    context = {'tasks':tasks}
    return render(req,'base/home.html',context )

def complete(req):
   return render(req,'base/complete.html')

def add_task(req):
   form = TaskFrom()
   if req.method =='POST':
      form = TaskFrom(req.POST)
      if form.is_valid():
        form.save()
        return redirect('home')
   context = {'form':form}
   return render(req,'base/task_form.html',context)

def update_task(req,pk):
   task = Task.objects.get(id=pk)
   form = TaskFrom(instance=task)
   context = {'form':form}
   if req.method =='POST':
      form = TaskFrom(req.POST,instance=task)
      if form.is_valid():
        form.save()
        return redirect('home')
   return render(req,'base/task_form.html',context)

def delete_task(req,pk):
   task = Task.objects.get(id=pk)
   context = {'obj':task}
   if req.method =='POST':
        task.delete()
        return redirect('home')
   return render(req,'base/delete.html',context)