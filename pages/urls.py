from django.urls import path
from .views import HomePageView, CareerPageView, AboutPageView, ContactPageView
from accounts.views import ApplicationPageView

urlpatterns = [
    path('career/', CareerPageView.as_view(), name='career'),
    path('accounts/application/', ApplicationPageView.as_view(), name='application'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
]
