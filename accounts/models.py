from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10)
    comments = models.TextField()
    sponsorship = models.BooleanField(default=False)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True)

    def get_absolute_url(self):
        return reverse('applicant_detail', args=[str(self.id)])
