from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('projects/show/<int:id>', views.show_project, name='show_project'),
]
