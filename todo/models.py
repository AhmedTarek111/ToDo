from django.db import models
from django.contrib.auth.models import User
import datetime

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_task')
    text = models.TextField(max_length=200)
    created_date =models.DateTimeField(default=datetime.datetime.now)


task_detail = (
        ('In Progress' ,'In Progress'),
        ('Completed' ,'Completed'),
    )

class TaskDetail(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name='task_detail_task')
    text = models.TextField(max_length=200)
    status = models.CharField(max_length=50,choices= task_detail)
