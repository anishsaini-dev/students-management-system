from django.urls import path
from . import views


urlpatterns = [
    path('', views.bade, name='bade'),
     path('', views.profile_list, name='profile_list'),
]