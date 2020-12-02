from django.shortcuts import render
from .models import City

def search_view(request):
    """
        with a location and an selected object, find the answer
    """

    Cities = City.objects.all()

    return render(request, 'search/search.html', { 'Cities':Cities})
