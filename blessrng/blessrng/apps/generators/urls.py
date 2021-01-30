from django.urls import path

from . import views

app_name = 'generators'
urlpatterns = [
    path('', views.index, name='index'),
    path('generate', views.generate, name='generate'),
    path('generate_pass', views.generate_pass, name='generate_pass'),
]
