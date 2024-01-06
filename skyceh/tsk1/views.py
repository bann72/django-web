from django.http import *
from django.shortcuts import render, redirect
from django.views import generic
from .models import Task
from .forms import PlasmaTaskForm
from django.urls import reverse_lazy


def add_plasma_task(request):  # Добавляем задачу для плазмы
    if request.method == "POST":
        taskform = PlasmaTaskForm(request.POST, request.FILES)
        if taskform.is_valid():
            taskform.save()
            return redirect("home")
        else:
            print(taskform.errors)
    else:
        taskform = PlasmaTaskForm()

    return render(request, "tasks/newtask.html", {"form": taskform})


class TaskView(generic.ListView):  # Отображение задач для плазмы
    model = Task
    template_name = "tasks/task_list.html"


class ComTaskView(generic.ListView):  # Отображение выполненных задач
    model = Task
    template_name = "tasks/completed_list.html"


class TaskDetailView(generic.DetailView):  # Детальная информация о задаче
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"
