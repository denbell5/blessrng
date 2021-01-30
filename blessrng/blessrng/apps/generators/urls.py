from django.urls import path

from . import views

app_name = 'generators'
urlpatterns = [
    path('', views.integer, name='integer'),
    path('integer', views.integer, name='integer'),
    path('generate_pass', views.generate_pass, name='generate_pass'),
]
