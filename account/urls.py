from django.urls import path
from . import views


urlpatterns = [
    path('', views.account_list_view, name='account_list'),
]