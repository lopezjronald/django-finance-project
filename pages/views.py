from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class CareerPageView(TemplateView):
    template_name = 'careers.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


