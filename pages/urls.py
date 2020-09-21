from django.urls import path
from .views import HomePageView, CareerPageView, AboutPageView, ContactPageView

urlpatterns = [
    path('career/', CareerPageView.as_view(), name='career'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
]
