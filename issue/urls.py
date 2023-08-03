from django.urls import path
from . import views


urlpatterns = [
    path('', views.issue_list_view, name='issue_list'),
]
