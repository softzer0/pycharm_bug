from django.urls import path
from .views import test_request

urlpatterns = [
    path('test/', test_request),
]
