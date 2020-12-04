from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.search_city, name = 'search_city'),
    path('<int:city_id>/', views.search_city, name = 'search_city'),
    path('<int:city_id>/<int:zone_id>/', views.search_city, name = 'search_city'),
]



#* for not generic view
# path('blog/', views.blog_index, name = 'blog_index'),
