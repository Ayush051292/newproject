from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, logout,  login
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import *
from django.db import connection
import os

def rawtodict(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def index(request):
    lst=[{'name':'ABC','age':20},{'name':'DEF','age':22},{'name':'GHI','age':21},{'name':'JKL','age':24},{'name':'MNO','age':23}]
    abc={'data':'120235','data1':'55555','lst':lst}
    return render(request,'home/home.html',abc)

def register(request):
    if request.method=='POST':
        u=User.objects.create(username=request.POST['username'])
        u.set_password(request.POST['password'])
        u.save()
        return redirect('/login/')
    return render(request,'home/register.html')

def login_page(request):
    if request.method=='POST':
        if User.objects.filter(username=request.POST['username']).exists():
            user=authenticate(request,username=request.POST['username'], password=request.POST['password'])
            if user is None:
                messages.success(request, "Wrong Password Given ...")
                return redirect('/login/')
            else:
                login(request,user)
                return redirect('/home/')
    return render(request,'home/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def user_index(request):
    val=emp.objects.all().values()  
    compact={'data':val}
    return render(request,'home/user_index.html',compact)

def user_add(request):
    if request.method=='POST':
        emp.objects.create(name=request.POST['name'],dob=request.POST['dob'],doj=request.POST['doj'],file=request.FILES['file'])
        messages.success(request, "User add successfully.")
        return redirect('/user_index/')
    return render(request,'home/user_add.html')

def user_edit(request,id):
    if request.method=='POST':
        emp.objects.filter(id=id).update(name=request.POST['name'],dob=request.POST['dob'],doj=request.POST['doj'])
        messages.success(request, "User updated successfully.")
        return redirect('/user_index/')
    data=emp.objects.get(id=id)
    compact={'data':data}
    return render(request,'home/user_edit.html',compact)

def user_show(request,id):
    val=emp.objects.get(id=id)
    compact={'data':val}
    return render(request, 'home/user_show.html',compact)

def user_delete(request,id):
    emp.objects.filter(id=id).delete()
    messages.success(request, "User deleted successfully.")
    return redirect('/user_index/')

def user_testing(request):
    if request.method=='POST':
        emp.objects.create(name=request.POST['test_name'],dob=request.POST['test_dob'],doj=request.POST['test_doj'])
        messages.success(request, "Test User added successfully.")
        return redirect('/user_index/')
    else:
        cursor=connection.cursor()
        cursor.execute("select name from home_emp where dob like '%2023-07%'")
        r=rawtodict(cursor)
        compact={'data': r}
        return render(request,'home/user_testing.html',compact)
    