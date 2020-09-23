from django.views.generic import TemplateView
from .models import Applicant


class ApplicationView(TemplateView):
    model = Applicant
    context_object_name = 'applicant'
    template_name = 'applicants/applicant_detail.html'
