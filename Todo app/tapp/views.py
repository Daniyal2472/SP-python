from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def index(request):
    if request.method=='POST':
        title=request.POST['title']
        Todo.objects.create(title=title)
        todos=Todo.objects.all()
        context={
            "todos":todos,
        }
        return render(request,'index.html',context)
    elif request.method == 'GET':
        todos = Todo.objects.all()
        context = {
            "todos":todos
        }
        return render(request, 'index.html', context)