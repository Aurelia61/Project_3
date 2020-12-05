from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    #todo change
    path('', views.home, name = 'home'),
    #todo path('article/<int:pk>/', views.DetailArticle.as_view(), name = 'article'),
]



#* for not generic view
# path('blog/', views.blog_index, name = 'blog_index'),
