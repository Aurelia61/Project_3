from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.BlogIndex.as_view(), name = 'blog_index'),
    path('article/<int:pk>/', views.DetailArticle.as_view(), name = 'article'),
]



#* for not generic view
# path('blog/', views.blog_index, name = 'blog_index'),
