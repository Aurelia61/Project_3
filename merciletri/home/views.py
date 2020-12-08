from django.shortcuts import render

def home(request):
    """
        #todo docstring
    """

    return render (request, 'home/home.html')