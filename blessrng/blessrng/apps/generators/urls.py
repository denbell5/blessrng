from django.urls import path
from generators.views.word_views import text

from . import views
from generators.views.pass_views import password
from generators.views.int_views import integer
from generators.views.stat_views import stat
from generators.views.all_entries_views import all_entries
from .data.constants.constants import Const

app_name = 'generators'
urlpatterns = [
    path('', integer, name=Const.Http.RandInt.name),
    path(
        Const.Http.RandInt.url,
        integer,
        name=Const.Http.RandInt.name
    ),
    path('password', password, name='password'),
    path('word', text, name='word'),
    path('stat', stat, name='stat'),
    path('all_entries', all_entries, name='all_entries')
]
