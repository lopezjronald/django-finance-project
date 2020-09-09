from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class CareerPageView(TemplateView):
    template_name = 'career.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class ApplicantPageView(TemplateView):
    template_name = 'applicant.html'
