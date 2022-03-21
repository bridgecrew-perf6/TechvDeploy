from django.contrib import admin

# Register your models here.

from .models import Project, Language, ProjectStage

admin.site.register(Project)
admin.site.register(Language)
admin.site.register(ProjectStage)
