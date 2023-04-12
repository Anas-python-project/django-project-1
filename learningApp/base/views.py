# from urllib import request

from django.shortcuts import render


tasks = [
    {'id':1,'task':'wakeup'},
    {'id':2,'task':'code'},
    {'id':3,'task':'sleep'}
]
userInfo ={'id':1,'userName':'Anas'}
# Create your views here.

def home(req,userName):
    context = {'tasks':tasks,'userInfo':userInfo,'userName':userName}
    return render(req,'base/home.html',context )

def complete(req,userName):
   context = {'userName':userName,'userInfo':userInfo}

   return render(req,'base/complete.html',context)