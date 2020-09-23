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
    technical_requirements = models.TextField()
    bonus_qualifications = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])


class Applicant(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applicants',
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    comments = models.TextField()
    sponsorship = models.BooleanField(default=False)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/')

    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)
