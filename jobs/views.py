from django.views.generic import ListView, DetailView
from .models import Job


class JobListView(ListView):
    model = Job
    context_object_name = 'job_list'
    template_name = 'jobs/job_list.html'


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'jobs/job_detail.html'
