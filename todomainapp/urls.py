"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from todomainapp.views import (
    hometasksList,
    newhometask,
    taskdetail,
    taskupdate,
    taskdelete,
    taskupdatestatus,
)

urlpatterns = [
    path("", hometasksList.as_view(), name="tasklist"),
    path("addtask/", newhometask.as_view(), name="newtask"),
    path("taskdetail/<int:taskid>", taskdetail.as_view(), name="taskdetail"),
    path("updatetask/<int:taskid>", taskupdate.as_view(), name="updatetask"),
    path("taskdelete/<int:taskid>", taskdelete.as_view(), name="taskdelete"),
    path("taskupdatestatus/", taskupdatestatus.as_view(), name="taskupdatestatus"),
]
