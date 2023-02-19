from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse
from datetime import datetime

import sys
sys.setrecursionlimit(1500)

from .models import *
from .forms import *

from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView

class hometasksList(ListView):

    model = hometasks
    template_name="todomainapp/main.html"


class newhometask(CreateView):
    def get(self, request, *args, **kwargs):
        model = hometasks
        form=addnewtask()
        context={'form':form}
    #template_name = "todomainapp/newtask.html"

        return render(request, 'todomainapp/newtask.html', context)


    def post(self, request):
        form=addnewtask(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/' )




class taskdetail(DetailView):
    model=hometasks
    pk_url_kwarg='taskid'
    template_name="todomainapp/taskdetail.html"

    def get_queryset(self, **kwargs):
        return hometasks.objects.filter(id=self.kwargs['taskid'])


class taskupdate(UpdateView):
    model=hometasks
    fields=['taskname', 'taskdescription']
    template_name_suffix = '_update_form'


    pk_url_kwarg='taskid'
    template_name="todomainapp/taskupdate.html"


class taskdelete(DeleteView):
    model=hometasks
    fields=['taskname','taskenddate'  ]
    template_name_suffix = '_update_form'


    pk_url_kwarg='taskid'
    template_name="todomainapp/taskupdate.html"
    def get(self, request,taskid):
        #taskedit = hometasks.objects.filter(id=self.kwargs['taskid'])
        taskedit = hometasks.objects.get(id=self.kwargs['taskid'])
        taskedit.delete()
        return redirect('/')

class taskupdatestatus(UpdateView):
    model = hometasks
    fields = ['taskname', 'taskenddate']

    def post(self, request,):
        if request.POST['action']=='1':
            taskedit = hometasks.objects.get(id=request.POST['id'])
            taskedit.taskstatus = request.POST['action']
            taskedit.taskenddate=None
            taskedit.save()

        else:
            taskedit = hometasks.objects.get(id=request.POST['id'])
            taskedit.taskstatus = request.POST['action']
            taskedit.taskenddate=datetime.now()
            taskedit.save()





        return HttpResponse('html')





