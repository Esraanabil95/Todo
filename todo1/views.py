# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todo_list": todos
    }
    return render(request , 'todo_list.html', context)


def fuck(request):
    return HttpResponse('what the fuck ')



def todo_detail(request , id):
    todo = Todo.objects.get( id = id)
    context = {
        "todo": todo
    }
    return render(request, "todo_detail.html", context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        pass
    context= {}
    return render(request, "todo_create.html", context)