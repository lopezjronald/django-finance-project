from django.urls import path
from .views import ApplicantListView, ApplicantDetailView

urlpatterns = [
    path('', ApplicantListView.as_view(), name='applicant_list'),
    path('<int:pk>/', ApplicantDetailView.as_view(), name='applicant_detail'),
]
