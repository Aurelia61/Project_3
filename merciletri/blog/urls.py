from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.BlogIndex.as_view(), name = 'blog_index'),
    path('article/<int:pk>', views.DetailArticle.as_view(), name = 'article'),
]

#todo mettre ou non un / après <int:pk> ? 
#todo car suivant les articles,
#todo le contenu s'affiche si l'url est trouvée 
#todo mais parfois il manque le / (ou il est en trop)

