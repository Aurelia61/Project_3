from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.home, name = 'home'),
    path('<int:city_id><str:city_name>/', views.home, name = 'home'),
    path('<int:city_id><str:city_name>/<int:zone_id><str:zone_name>/', views.home, name = 'home'),

]
