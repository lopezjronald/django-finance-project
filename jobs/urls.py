from django.urls import path
from .views import JobListView, JobDetailView

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<uuid:pk>/', JobDetailView.as_view(), name='job_detail'),
]
