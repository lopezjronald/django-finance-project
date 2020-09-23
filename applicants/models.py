import uuid

from django.db import models
from django.urls import reverse


class Applicant(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        editable=False,
        default=uuid.uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    comments = models.TextField()
    sponsorship = models.BooleanField(default=False)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])
