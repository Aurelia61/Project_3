from django.shortcuts import render
from django.views import generic

from .models import Article


class BlogIndex(generic.ListView):
    """
        manage the blog index page thanks to django generic list view
    """

    # path to the template for this view
    template_name = "blog/blog_index.html"

    # which context is concerned by this view
    context_object_name = 'latest_articles'

    def get_queryset(self):
        """
            get and return the last 3 articles registred in the databases
        """

        articles_list_index = (Article.objects
            #todo ranger par date et non par id
            .order_by("-id")
            # the 3 latest
            [:10]
        )

        # Return the list of the 3 lastest article
        return articles_list_index


class DetailArticle(generic.DetailView):
    """
        manage the article page thanks to django generic detail view
    """

    # what model is concerned by this view
    model = Article

    # path to the template for this view
    template_name = "blog/article.html"



#! avant les vues génériques
# def article(request, name):
#     """
#         manage what it will be contain on article page
#     """

#     article = Article.objects.get(title=name)
#     dict_article = {'article' : article}

#     return render(request, 'blog/article.html', dict_article)


# def blog_index(request):
#     """
#         manage what it will be contain on the blog index
#     """

#     articles = Article.objects.all()
#     dict_articles = {'articles': articles}


#     return render(request, 'blog/blog_index.html', dict_articles)
