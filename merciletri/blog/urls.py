from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.BlogIndex.as_view(), name = 'blog_index'),
    path('article/<int:pk>', views.DetailArticle.as_view(), name = 'article'),
    path('article/<int:pk><int:city_id><str:city_name>/', views.search_on_article_page),
    path('article/<int:pk><int:city_id><str:city_name>/<int:zone_id><str:zone_name>/', views.search_on_article_page),
]
