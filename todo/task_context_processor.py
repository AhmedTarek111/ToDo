from .models import Task,TaskDetail

def create_task(request):
    user = request.user
    task,created =Task.objects.get_or_create(user=user)
    if request.user.is_authenticated:
        if not created :
            task_detail = TaskDetail.objects.filter(task = task)
            return {'task_detail':task_detail ,'task':task}
        else:
            return {'task':task}
    else:
        return {}
        