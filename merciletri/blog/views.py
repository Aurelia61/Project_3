from django.shortcuts import render
from django.views import generic

from .models import Article
from search.models import City, CollectLocation, Zone, Garbage, GarbageType


def search_on_article_page(request, city_id=None, zone_id=None, city_name=None, zone_name=None, garbage_name=None):
    """
        get the city
    """

    city_image = ""
    cities = City.objects.all()
    city_name = city_name
    zones = None
    zone_name = zone_name
    garbages = None
    type_id = None
    selected_garbage = None
    garbage_locations = []
    garbage_name = garbage_name
    
    if request.method == "POST":

        if city_id is None and zone_id is None:
            selected_city = request.POST.get("selected_city", None)
            print (f" ville : {selected_city}")

            for city in cities :
                if selected_city == city.name :
                    city_image = city.image.url
                    city_id = city.id
                    city_name = city.name
                    break;

            zones = Zone.objects.filter(city_id=city_id)
            print(f"toutes les zones de la ville : {zones}")
        
        elif zone_id is None:
            zones = Zone.objects.filter(city_id=city_id)
            print(f"toutes les zones de la ville : {zones}")
            
            selected_zone = request.POST.get("selected_zone", None)
            print (f"zone : {selected_zone}")

            for zone in zones :
                if selected_zone == zone.name :
                    zone_id = zone.id
                    zone_name = zone.name
                    break;

            garbages = Garbage.objects.all()
            print(f"tous les déchets de la ville : {garbages}")

        else:

            garbages = Garbage.objects.all()
            print(f"tous les déchets de la ville : {garbages}")
            
            selected_garbage = request.POST.get("selected_garbage", None)
            print (f"déchet : {selected_garbage}")

            type_id = None
            #todo faire des compréhensions de liste
            for garbage in garbages :
                if selected_garbage == garbage.name :
                    type_id = garbage.garbagetype_id
                    garbage_name = garbage.name
                    break;
                    print(f"Type : {type_id}")

    return render(
        request, 
        'blog/article.html', 
        {
            "cities": cities, 
            "city_image": city_image, 
            "city_id": city_id,
            "city_name": city_name,
            "zones": zones, 
            "zone_id": zone_id,
            "zone_name": zone_name,
            "garbages": garbages, 
            "selected_garbage": selected_garbage,
            "garbage_locations": garbage_locations,
            "garbage_name" : garbage_name,
            # "garbage_loc_day_time": garbage_loc_day_time
        })

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

