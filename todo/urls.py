from django.urls import path
from .views import *

app_name = 'todo'

urlpatterns = [
    path('', main, name='main'),  
    path('add_task_detail/', add_task_detail, name='add_task_detail'),
    path('delete_task_detail/<int:pk>', DeleteTaskDetail.as_view(), name='delete_task_detail'),
    path('update_status/<int:pk>',changestatus,name='update')
]
