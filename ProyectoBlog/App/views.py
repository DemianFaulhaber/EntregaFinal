"""""
from msilib.schema import tables
from re import template
from xml.dom.minidom import Document
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Post
from App import templates
from django.contrib import messages
from django.forms import ModelForm
from .forms import *
"""
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib import messages


def eliminar(request, post_id):
    post = Post.objects.get(id= post_id)
    post.delete()
    return redirect('inicio')



def postear(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()

    context = {'form' : form}
    return render(request, 'postear.html', context)


def home(request):   
    return render(request,"home.html")

def sobre(request):
    return render(request, 'aboutme.html')

def feed(request):
    posteos = Post.objects.all()
    context = {'posteos':posteos}
    return render(request,"feed.html", context)    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'register.html', context) 