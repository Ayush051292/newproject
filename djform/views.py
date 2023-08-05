from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import *
from .forms import DjformForm
import datetime
from bs4 import BeautifulSoup


def index(request):
    data=Djform.objects.all()
    return render(request,'djform/index.html',{'data':data})

def add(request):
    if request.method=="POST":
        # return HttpResponse(request.POST['text_area'])
        form=DjformForm(request.POST)
        if form.is_valid():
            form.save()
    compact={'form':DjformForm}
    return render(request,'djform/add.html',compact)

def edit(request,id):
    data=Djform.objects.get(id=id)
    form=DjformForm(instance=data)
    compact={'form':form,'id':id, 'data':data}
    return render(request,'djform/edit.html',compact)

def show(request,id):
    data=Djform.objects.get(id=id)
    compact={'data':data}
    return render(request,'djform/show.html',compact)

def delete(request,id):
    Djform.objects.filter(id=id).delete()
    return redirect('/djform/index')

def autosave(request):
    id=request.GET.get('id')
    text=request.GET.get('text')
    raw_text = BeautifulSoup(text, "html.parser").text
    wc=len(raw_text.split())
    Djform.objects.filter(id=id).update(text_area=text,updated_at=datetime.datetime.now(),word_count=wc)

    data={'count':wc}
    return JsonResponse(data)