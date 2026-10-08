from django.urls import path
from . import views

app_name = 'homebastian'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('homebastian/', views.inicio, name='homebastian'),
]