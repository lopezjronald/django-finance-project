from django.contrib import admin
from .models import Job, Requirement, Qualification


class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 3


class QualificationInline(admin.TabularInline):
    model = Qualification
    extra = 3


class JobAdmin(admin.ModelAdmin):
    inlines = [
        RequirementInline,
        QualificationInline,
    ]
    list_display = ('title', 'location')


admin.site.register(Job, JobAdmin)
