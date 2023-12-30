from django.urls import path

from . import views

urlpatterns = [
    path("", views.read_view, name='read_view'),
]