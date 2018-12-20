from .task import my_task
from django.shortcuts import render
from django.conf import settings

def progress_view(request, time):
    result = my_task.delay(int(time))
    return render(request, 'progress_bar/display_progress.html', context={'task_id': result.task_id})