from django.urls import path
from .api import DashboardView

urlpatterns = [
    path('api/dashboard/', DashboardView.as_view(), name='dashboard'),
]
