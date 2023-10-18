from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DeleteView 
from .models import *

def main(request):
    return render(request ,'index.html')

def add_task_detail(request):
    user= request.user
    task = Task.objects.get(user=user)
    text = request.POST['task_detail_text']
    task_detail = TaskDetail.objects.create(task=task ,text=text)

    context ={
        'task_detail':TaskDetail.objects.all()
    }
    return redirect('/')  

class DeleteTaskDetail(DeleteView):
    model= TaskDetail
    success_url = '/'