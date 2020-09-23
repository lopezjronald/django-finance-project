from django.contrib import admin
from .models import Applicant


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'sponsorship')


admin.site.register(Applicant, ApplicantAdmin)
