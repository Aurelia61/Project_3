# imports
from django.urls import path, include

# models imports
from . import views

# namespace
app_name = 'game'

# routes
urlpatterns = [
    path("", views.game, name="game"),
    # path("<int:garbage_id>/", views.game, name="game"),
]