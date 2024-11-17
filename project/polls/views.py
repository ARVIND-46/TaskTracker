from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required


# Create your views here.
def taskList(request):
    return render(request,'polls/taskList.html')

def addTask(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        priority = request.POST.get("priority")
        status = request.POST.get("status")
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status=status,
        )
        return redirect("task_list")  # Redirect to the task list view

    return render(request,'polls/addTask.html')
''''
def task_list(request):
    tasks = Task.objects.all()  # Retrieve all tasks from the database
    return render(request, 'polls/displayTL.html', {'tasks': tasks})
    '''
def display_tasks(request):
    # Separate tasks into pending and completed
    pending_tasks = Task.objects.filter(status='Pending')
    completed_tasks = Task.objects.filter(status='Completed')

    # Pass both lists to the template
    context = {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'polls/displayTL.html', context)



#def delTask:
#def editTask:
