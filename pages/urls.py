from django.urls import path
from .views import HomePageView, CareerPageView, AboutPageView, ContactPageView
from accounts.views import SignupPageView

urlpatterns = [
    path('career/', CareerPageView.as_view(), name='career'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
]
