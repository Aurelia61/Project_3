from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.home, name = 'home'),
]
