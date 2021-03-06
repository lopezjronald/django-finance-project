from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class CareerPageView(TemplateView):
    template_name = 'job_list.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


