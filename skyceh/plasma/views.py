from django.shortcuts import render, redirect, get_object_or_404
from tsk1.models import Task
from .forms import DoPT

# Create your views here.


def view_plasma_task(request):
    tasks = Task.objects.filter(spot="плазма")
    return render(request, "tasks/plasma/task_list.html", {"tasks": tasks})


def view_com_plasma_task(request):
    tasks = Task.objects.filter(spot="плазма")
    return render(request, "tasks/plasma/completed_list.html", {"tasks": tasks})


def do_plasma_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = DoPT()
    if request.method == "POST":
        rdy = request.POST.get("rdy")
        task.now = rdy
        if int(task.now) == int(task.total):
            task.ready = True
        task.save()
        return render(
            request, "tasks/plasma/do_plasma_task.html", {"task": task, "form": form}
        )
    return render(
        request, "tasks/plasma/do_plasma_task.html", {"task": task, "form": form}
    )
