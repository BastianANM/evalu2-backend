from django.urls import path
from . import views

app_name = 'homebastian'

urlpatterns = [
    path('home1', views.home1, name='home1'),
]