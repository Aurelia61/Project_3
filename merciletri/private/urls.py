from django.urls import path, include
from . import views

app_name = 'private'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    # path('private/', name = 'private'),
]
