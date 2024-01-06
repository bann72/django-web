from django.views import generic
from django.urls import reverse_lazy
from .models import TaskList, SpotList

# Create your views here.


class SpotListCreate(generic.CreateView):
    model = SpotList
    fields = ["man", "spot"]
    template_name = "tasks/spot_create.html"
    success_url = reverse_lazy("home")  # Перенаправление после успешного создания


class TaskListCreate(generic.CreateView):
    model = TaskList
    fields = ["date", "task", "file", "man", "deadline"]
    template_name = "tasks/task_create.html"
    success_url = reverse_lazy("home")  # Перенаправление после успешного создания
