from django.db import models




# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a project language (e.g. python django)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the project')

    # ManyToManyField used because Language can contain many project.
    language = models.ManyToManyField(Language, help_text='Select a Languages for this project')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class ProjectStage(models.Model):
    project = models.ForeignKey('Project', on_delete=models.RESTRICT, null=True)
    environment = models.CharField(max_length=200)

    host = models.CharField(max_length=200,default='localhost')
    script_location = models.CharField(max_length=200)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the project stage')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.project.title} ({self.environment})'
