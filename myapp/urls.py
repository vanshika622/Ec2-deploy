from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world),  # This maps the root URL to the hello_world view
]
