"""
URL configuration for skyceh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from orders import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from tsk1.views import (
    add_plasma_task,
    TaskView,
    TaskDetailView,
    ComTaskView,
)
from orders.views import OrdInvList
from plasma.views import (
    view_plasma_task,
    view_com_plasma_task,
    do_plasma_task,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_required(views.OrderListView.as_view()), name="home"),
    path("statusupdate/<int:znum>", login_required(views.StatusUpdate), name="stupd"),
    path(
        "create/", login_required(views.OrderCreateView.as_view()), name="order_create"
    ),
    re_path(r"^orders/$", login_required(views.OrderListView.as_view()), name="orders"),
    re_path(
        r"^complete/$", login_required(views.ComOrderView.as_view()), name="com-orders"
    ),
    re_path(
        r"^order/(?P<pk>\d+)$",
        login_required(views.OrderDetailView.as_view()),
        name="order-detail",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    re_path("logout/", login_required(views.logout_view), name="logout"),
    re_path(r"^inv/(?P<pk>\d+)$", login_required(OrdInvList), name="invsort"),
    path("newplasmatask/", login_required(add_plasma_task), name="newplasmatask"),
    path("task/", login_required(TaskView.as_view()), name="task"),
    path(
        "task/<int:pk>/", login_required(TaskDetailView.as_view()), name="task-detail"
    ),
    path("plasma/task/", login_required(view_plasma_task), name="plasma_task"),
    path("dptask/<int:pk>/", login_required(do_plasma_task), name="do_plasma_task"),
    re_path(
        r"^task/complete/$", login_required(ComTaskView.as_view()), name="com-task"
    ),
    path(
        "plasma/comtask/", login_required(view_com_plasma_task), name="plasma_com_task"
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
