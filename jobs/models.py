from django.db import models


class Jobs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technical_requirements = models.CharField(max_length=500)
    bonus_qualifications = models.CharField(max_length=500)
