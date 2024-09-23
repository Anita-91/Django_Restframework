from django.contrib import admin

# Register your models here.
from .models import Manager, Project, Task

# Register your models here.
admin.site.register(Manager)
admin.site.register(Project)
admin.site.register(Task)