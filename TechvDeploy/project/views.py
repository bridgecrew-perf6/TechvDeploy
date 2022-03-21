from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Project, ProjectStage
# Create your views here.



def index(request):
    """View function for projects page of site."""

    # # Generate counts of some of the main objects
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    #
    # # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    #
    # # The 'all()' is implied by default.
    # num_authors = Author.objects.count()
    #
    # context = {
    #     'num_books': num_books,
    #     'num_instances': num_instances,
    #     'num_instances_available': num_instances_available,
    #     'num_authors': num_authors,
    # }
    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context = context)


def projects(request):
    projects = Project.objects.all()
    return render(request,'projects.html', context = {'projects':projects})

def show_project(request,id):
    project = get_object_or_404(Project, id=id)
    project_stages = ProjectStage.objects.filter(project=project)
    return render(request,'show_project.html', context = {'project':project,'project_stages':project_stages})
