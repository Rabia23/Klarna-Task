"""Api urls file."""
from django.urls import path

from apps.api.views import FunctionLogsListAPIView, MathAPIView

urlpatterns = [
    path("math/", MathAPIView.as_view(), name="math"),
    path("func-logs/", FunctionLogsListAPIView.as_view(), name="func-logs"),
]
