from django.contrib import admin
from .models import Language, Tool, Job

admin.site.register(Job)
admin.site.register(Language)
admin.site.register(Tool)