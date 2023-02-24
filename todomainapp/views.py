import sys
from datetime import datetime
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .serializers import TasksSerializer
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import *

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class hometasksList(ListView):
    model = hometasks
    template_name = "todomainapp/main.html"


class newhometask(CreateView):
    def get(self, request, *args, **kwargs):
        model = hometasks
        form = addnewtask()
        context = {"form": form}

        return render(request, "todomainapp/newtask.html", context)

    def post(self, request):
        form = addnewtask(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


class taskdetail(DetailView):
    model = hometasks
    pk_url_kwarg = "taskid"
    template_name = "todomainapp/taskdetail.html"

    def get_queryset(self, **kwargs):
        return hometasks.objects.filter(id=self.kwargs["taskid"])


class taskupdate(UpdateView):
    model = hometasks
    fields = ["taskname", "taskdescription"]
    template_name_suffix = "_update_form"

    pk_url_kwarg = "taskid"
    template_name = "todomainapp/taskupdate.html"


class taskdelete(DeleteView):
    model = hometasks
    fields = ["taskname", "taskenddate"]
    template_name_suffix = "_update_form"

    pk_url_kwarg = "taskid"
    template_name = "todomainapp/taskupdate.html"

    def get(self, request, taskid):
        taskedit = hometasks.objects.get(id=self.kwargs["taskid"])
        taskedit.delete()
        return redirect("/")


class taskupdatestatus(UpdateView):
    model = hometasks
    fields = ["taskname", "taskenddate"]

    def post(
        self,
        request,
    ):
        if request.POST["action"] == "1":
            taskedit = hometasks.objects.get(id=request.POST["id"])
            taskedit.taskstatus = request.POST["action"]
            taskedit.taskenddate = None
            taskedit.save()

        else:
            taskedit = hometasks.objects.get(id=request.POST["id"])
            taskedit.taskstatus = request.POST["action"]
            taskedit.taskenddate = datetime.now()
            taskedit.save()

        return HttpResponse("html")


class TaskPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 20


class TaskAPIView(generics.ListAPIView):
    queryset = hometasks.objects.all()
    serializer_class = TasksSerializer
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["taskstatus", "taskcreatedate"]
    filterset_fields = ["taskname", "taskstatus"]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return hometasks.objects.all()
        return hometasks.objects.filter(pk=pk)

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class TaskEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = hometasks.objects.all()
    serializer_class = TasksSerializer


class createTaskAPIView(APIView):
    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
