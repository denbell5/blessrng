from django.urls import path

from . import views
from .data.constants.constants import Const

app_name = 'generators'
urlpatterns = [
    path('', views.integer, name=Const.Http.RandInt.name),
    path(
        Const.Http.RandInt.url,
        views.integer,
        name=Const.Http.RandInt.name
    ),
    path('password', views.password, name='password'),
]
