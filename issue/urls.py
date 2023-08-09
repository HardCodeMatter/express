from django.urls import path
from . import views


urlpatterns = [
    path('', views.issue_list_view, name='issue_list'),
    path('<int:id>/', views.issue_detail_view, name='issue_detail'),
    path('create/', views.issue_create_view, name='issue_create'),

    path('tags/', views.tag_list_view, name='tag_list'),
    path('tags/<int:tag_id>/', views.issue_list_by_tag_view, name='issue_list_by_tag'),
    path('tags/create/', views.tag_create_view, name='tag_create'),
]
