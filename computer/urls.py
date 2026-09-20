from django.urls import path
from . import views

urlpatterns = [
    path('', views.router, name='router')
]