from django.urls import path
from . import view

urlpatterns = [
    path('', view.apiOverview, name="api-overview")
]