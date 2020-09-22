from django.views.generic import ListView, DetailView
from .models import Applicant


class ApplicantListView(ListView):
    model = Applicant
    context_object_name = 'applicant_list'
    template_name = 'applicants/applicant_list.html'


class ApplicantDetailView(DetailView):
    model = Applicant
    context_object_name = 'applicant'
    template_name = 'applicants/applicant_detail.html'
