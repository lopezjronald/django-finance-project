import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Job(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])





class Requirement(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='requirements',
    )
    technical_requirement = models.CharField(max_length=255)

    def __str__(self):
        return self.technical_requirement


class Qualification(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='qualifications',
    )
    bonus_qualification = models.CharField(max_length=255)

    def __str__(self):
        return self.bonus_qualification
