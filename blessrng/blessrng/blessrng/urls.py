"""
Definition of urls for blessrng.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.contrib.auth import logout
from django.conf import settings

urlpatterns = [
    path('', include('generators.urls')),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context={
                 'title': 'Log in',
                 'year': datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('generators/', include('generators.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout,
         {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
