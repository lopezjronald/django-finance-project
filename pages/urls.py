from django.urls import path

from .views import HomePageView, AboutPageView, CareerPageView, ContactPageView

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('career/', CareerPageView.as_view(), name='career'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
