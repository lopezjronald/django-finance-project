from django.urls import path
from .views import ApplicationPageView

urlpatterns = [
    path('application/', ApplicationPageView.as_view(), name='application'),
]
