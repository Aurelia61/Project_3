from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.search_city, name = 'search_city'),
    path('<int:city_id><str:city_name>/', views.search_city, name = 'search_city'),
    path('<int:city_id><str:city_name>/<int:zone_id><str:zone_name>/', views.search_city, name = 'search_city'),
]



#* for not generic view
# path('blog/', views.blog_index, name = 'blog_index'),
