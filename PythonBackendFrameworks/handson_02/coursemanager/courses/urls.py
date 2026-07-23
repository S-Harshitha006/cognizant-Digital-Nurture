# Defines URL routes that map incoming requests to views.
from django.urls import path
from .views import hello_view

urlpatterns = [
    path("hello/", hello_view, name="hello"),
]