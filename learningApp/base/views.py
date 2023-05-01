# from urllib import request

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskFrom


userInfo ={'id':'anas','userName':'Anas'}
# Create your views here.

def home(req):
    tasks = Task.objects.filter(user_id=2)
    if req.method =='POST':
        form = TaskFrom(req.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')

    context = {'tasks':tasks,'userInfo':userInfo}
    return render(req,'base/home.html',context )

def complete(req,userName):
   context = {'userName':userName,'userInfo':userInfo}
   return render(req,'base/complete.html',context)

def add_task(req):
   form = TaskFrom()
   if req.method =='POST':
      form = TaskFrom(req.POST)
      if form.is_valid():
        form.save()
        return redirect('home')
   context = {'userInfo':userInfo,'form':form}
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