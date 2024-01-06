from django.http import *
from .models import MainOrderInfo
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render
from .forms import OrderForm


class OrderListView(generic.ListView):
    model = MainOrderInfo


class ComOrderView(generic.ListView):
    model = MainOrderInfo
    template_name = "orders/completed_list.html"


class OrderDetailView(generic.DetailView):
    model = MainOrderInfo


def StatusUpdate(request, znum):
    try:
        inf = MainOrderInfo.objects.get(znum=znum)
        if inf.status == "В работе":
            MainOrderInfo.objects.filter(znum=znum).update(status="Выполнен")
        else:
            MainOrderInfo.objects.filter(znum=znum).update(status="В работе")
        return HttpResponseRedirect("/")
    except MainOrderInfo.DoesNotExist:
        return HttpResponseNotFound("<h2>Заказ не найден</h2>")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


class OrderCreateView(generic.CreateView):
    model = MainOrderInfo
    form_class = OrderForm
    template_name = "orders/order_create.html"
    success_url = reverse_lazy("orders")  # Перенаправление после успешного создания


def OrdInvList(request, pk):
    try:
        zak = MainOrderInfo.objects.get(znum=pk)
        num = zak.invorder
        inv = MainOrderInfo.objects.filter(invorder=num)
        return render(request, "orders/inv_list.html", {"inv": inv})
    except MainOrderInfo.DoesNotExist:
        return HttpResponseNotFound("<h2>Счет не найлен</h2>")
