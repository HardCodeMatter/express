from django.urls import path
from . import views


urlpatterns = [
    path('', views.render, name='issue_list'),
]