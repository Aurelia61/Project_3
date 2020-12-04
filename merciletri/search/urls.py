from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.search_city, name = 'search_city'),
    path('<int:city_id>', views.search_zone, name = 'search_zone'),
    path('<int:pk>/', views.search_garbage, name = 'search_garbage'),
]



#* for not generic view
# path('blog/', views.blog_index, name = 'blog_index'),
