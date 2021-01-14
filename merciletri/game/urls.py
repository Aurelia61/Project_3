from django.urls import path, include
from . import views

app_name = 'game'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.game, name="game")
]
