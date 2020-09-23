# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from jobs.models import Job


class ApplicationPageView(generic.CreateView):
    model = Job
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'applicants/applicant_detail.html'
