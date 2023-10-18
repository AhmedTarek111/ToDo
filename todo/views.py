from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DeleteView ,UpdateView
from .models import *
def main(request):
    return render(request ,'index.html')

def add_task_detail(request):
    if request.method == 'POST':
        user = request.user
        task = Task.objects.get(user=user)
        text = request.POST.get('task_detail_text')
        task_detail = TaskDetail.objects.create(task=task, text=text)
        return redirect('/')


class DeleteTaskDetail(DeleteView):
    model= TaskDetail
    success_url = '/'

def changestatus(request,pk):
    data = TaskDetail.objects.get(id=pk)
    if data.status == "completed":
        data.status = "In Progress"
        data.save()
    else:
        data.status = "completed" 
        data.save()    
    return redirect('/')
