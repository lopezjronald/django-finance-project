from django.db import models


class Applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    comments = models.TextField()
    sponsorship = models.BooleanField(default=False)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True)

    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)
