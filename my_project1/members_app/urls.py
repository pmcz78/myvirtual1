from django.urls import path
from . import views

urlpatterns = [
    path('members_app/', views.members_app, name='members_app'),
]