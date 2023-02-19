from django.contrib import admin

from .models import hometasks


class hometasksdmin(admin.ModelAdmin):
    list_display = ("taskname", "taskdescription", "taskcreatedate", "taskenddate")
    search_fields = (
        "taskname",
        "taskdescription",
    )


admin.site.register(hometasks, hometasksdmin)
