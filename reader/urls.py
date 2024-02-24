from django.urls import path

from . import views

urlpatterns = [
    path("read", views.read_view, name="read_view"),
    path("search", views.search_view, name="search_view"),
    path("sources", views.sources_view, name="sources_view"),
]
