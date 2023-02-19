from django.db import models
from django.utils import timezone
from django.urls import reverse # Новый импорт


class hometasks(models.Model):
    taskname = models.CharField(max_length=150,blank=True,null=True )
    taskdescription = models.CharField(max_length=150,blank=True,null=True )
    taskenddate = models.DateTimeField( null=True)
    taskcreatedate = models.DateTimeField(default=timezone.now, null=True)
    taskstatus=models.IntegerField(default=1, blank=True,null=True)

    def __str__(self):
        return self.taskname

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('taskdetail', args=[str(self.id)])