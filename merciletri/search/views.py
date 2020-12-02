from django.shortcuts import render

def search_view(request):
    """
        with a location and an selected object, find the answer
    """

    return render(request, 'search/search.html')
