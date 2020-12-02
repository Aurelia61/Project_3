from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    #todo change
    path('', views.search_view, name = 'search_view'),
    #todo path('article/<int:pk>/', views.DetailArticle.as_view(), name = 'article'),
]



#* for not generic view
# path('blog/', views.blog_index, name = 'blog_index'),
