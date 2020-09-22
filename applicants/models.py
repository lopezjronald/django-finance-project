from django.db import models
from django.urls import reverse


class Applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    comments = models.TextField()
    sponsorship = models.BooleanField(default=False)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/')

    def __str__(self):
        template = '{0.first_name} {0.last_name} Sponsorship: {0.sponsorship}'
        return template.format(self)

    def get_absolute_url(self):
        return reverse('applicant_detail', args=[str(self.id)])
