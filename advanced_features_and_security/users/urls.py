from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view/', views.view_content, name='view_content'),
    path('create/', views.create_content, name='create_content'),
    path('edit/', views.edit_content, name='edit_content'),
    path('delete/', views.delete_content, name='delete_content'),
]
