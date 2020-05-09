from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'CoronaUpdater'
urlpatterns = [ path('', views.home, name='home'),
                path('details.html', views.details, name='details'),
              ]
