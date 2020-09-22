from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technical_requirements = models.TextField()
    bonus_qualifications = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # applicant = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    #     related_name='jobs')

    def __str__(self):
        return self.title


# class Applicant(models.Model):
#     job = models.ForeignKey(
#         Job,
#         on_delete=models.CASCADE,
#         related_name='jobs',
#     )
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=10)
#     comments = models.TextField()
#     sponsorship = models.BooleanField(default=False)
#     resume = models.FileField(upload_to='resumes/')
#     cover_letter = models.FileField(upload_to='cover_letters/')
#
#     def __str__(self):
#         template = '{0.first_name} {0.last_name} Sponsorship: {0.sponsorship}'
#         return template.format(self)
