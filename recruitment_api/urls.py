from django.urls import path

from .views import HrAPIView

urlpatterns = [
    path('', HrAPIView.as_view())
]
