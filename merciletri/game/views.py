from django.shortcuts import render
from search.models import City, CollectLocation, Zone, Garbage, GarbageType

import random


def game(request, garbage_id=None):
    """

    """

    running = False
    dest_resultat=False
    garbages=None
    destinations = []
    selected_garbage=None
    image=None
    resultat=""

    if request.method == "POST":
        ask_running = request.POST.get("ask_running", None)
        selected_destination = request.POST.get ("selected_destination", None)

        if ask_running :
            running = True

            # get image of one garbage randomly
            selected_garbage = random.choice(Garbage.objects.all())
            image = selected_garbage.image
            garbage_id = selected_garbage.id

            # get all the garbages
            garbages = Garbage.objects.all()

            # get all destinations without duplicates 
            for dest in garbages:
                destinations.append(dest.destination)
            destinations = list(dict.fromkeys(destinations))

        if selected_destination:
            import pdb; pdb.set_trace()
            dest_resultat = True
            garbage = Garbage.objects.filter(id=garbage_id)
            for garb in garbage:
                if selected_destination == garb.destination:
                    resultat = "C'est gagné !"
                else:
                    resultat = "Perdu"


    return render(
        request, 
        'game/game.html',
        {
            "Garbages" : garbages,
            "Destinations" : destinations,
            "Selected_garbage" : selected_garbage,
            "Image" : image,
            "Garbage_id": garbage_id,
            "Dest_resultat" : dest_resultat,
            "Resultat" : resultat,
            "Running": running,
        })
