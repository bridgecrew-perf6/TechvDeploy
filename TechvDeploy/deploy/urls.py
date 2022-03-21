from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.deployments, name='deployments'),
    path('run/<int:id>/', views.deploy_project, name='deploy_project'),
    path('deploy-results/<uuid>/', views.deploy_results, name='deploy_results'),
]
