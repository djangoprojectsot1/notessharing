from django.urls import path
from .views import Registerview

urlpatterns = [
    path('', Registerview.as_view())
]
