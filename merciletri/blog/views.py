from django.shortcuts import render
from django.views import generic

from .models import Article

def blog_index(request):
    """
        manage what it will be contain on the blog index
    """

    articles = Article.objects.all()
    dict_articles = {'articles': articles}


    return render(request, 'blog/blog_index.html', dict_articles)




class DetailArticle(generic.DetailView):
    """
        manage the article page thanks to django generic detail view
    """

    model = Article
    template_name = "blog/article.html"



#! avant les vues génériques
# def article(request, name):
#     """
#         manage what it will be contain on article page
#     """

#     article = Article.objects.get(title=name)
#     dict_article = {'article' : article}

#     return render(request, 'blog/article.html', dict_article)