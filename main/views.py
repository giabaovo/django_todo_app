from django.shortcuts import render, redirect, get_object_or_404

from main.models import TaskModel

# def home(request):
#     return render(request, "home.html")

def tasks_list(request):
    tasks = TaskModel.objects.filter(is_done=False)
    complete_tasks = TaskModel.objects.filter(is_done=True)
    return render(request, "home.html", context={"tasks": tasks, "complete_tasks": complete_tasks})

def add_task(request):
    task_title = request.POST["task-name"]
    TaskModel.objects.create(title=task_title)
    return redirect("home")

def edit_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    if request.method == "POST":
        task_title = request.POST["task-name-edit"]
        task.title = task_title
        task.save()
        return redirect("home")
    else:
        return render(request, "edit_task.html", context={"task": task})
    
def delete_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.delete()
    return redirect("home")


def task_status(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("home")