from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


class DeploymentInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='deployment id')
    project_stage = models.ForeignKey('project.ProjectStage', on_delete=models.RESTRICT, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    DEPLOYMENT_STATUS = (
        ('s', 'Success'),
        ('e', 'Error'),
        ('p', 'pending'),
        ('u', 'Unknown'),
    )

    status = models.CharField(
        max_length=1,
        choices=DEPLOYMENT_STATUS,
        blank=True,
        default='u',
        help_text='Project DEPLOYMENT_STATUS status',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.project_stage.project.title})'
