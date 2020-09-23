from django.contrib import admin
from .models import Job, Applicant


class ApplicantInline(admin.StackedInline):
    model = Applicant


class JobAdmin(admin.ModelAdmin):
    inlines = [
        ApplicantInline,
    ]
    list_display = ('title', 'location',)


admin.site.register(Job, JobAdmin)
