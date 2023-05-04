from django.contrib import admin
from .models import Tag, Task
# Register your models here.


admin.site.register(Tag)


class Taskmanager(admin.ModelAdmin):
    filter_horizontal = [ 'tags']

admin.site.register(Task, Taskmanager)