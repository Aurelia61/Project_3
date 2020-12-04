from django.shortcuts import render
from .models import City, CollectLocation, Zone, Garbage, GarbageType

def search_city(request):
    """
        get the city
    """

    city_image =""
    city_id = None
    cities = City.objects.all()

    if request.method == "POST":
        selected_city = request.POST.get("selected_city", None)
        print (f" ville : {selected_city}")

        for city in cities :
            if selected_city == city.name :
                city_image = city.image.url
                city_id = city.id
                print(f"city_id : {city_id}")
    
    return render(request, 'search/search.html', {"cities":cities, "city_image": city_image, "city_id":city_id})


def search_zone(request, city_id):
    """
        get the zone
    """

    zone_id = None

    zones = Zone.objects.all()
    print(f"toutes les zones : {zones}")
    selected_zone = request.POST.get("selected_zone", None)
    print (f"zone : {selected_zone}")


    for zone in zones :
        print(f"Id de la ville de la zone : {zone.city_id}")
        if zone.city_id == city_id:
            if selected_zone == zone.name :
                zone_id = zone.id
                print(f"Zone : {zone_id}")

    return render(request, 'search/search.html', {"zones":zones, "selected_zone": selected_zone, "zone_id":zone_id})



def search_garbage(request, city_id, zone_id):
    """
        get the garbage type
    """

    type_id = None

    garbages = Garbage.objects.all()

    # garbagetypes = GarbageType.object.all()

    selected_garbage = request.POST.get("selected_garbage", None)
    print (f"déchet : {selected_garbage}")

    for garbage in garbages :
        if selected_garbage == garbage.name :
            type_id = garbage.garbagetype_id
            print(f"Type : {type_id}")

    # type = GarbageType.objects.filter(name = selected_garbage)
    # print(f"type : {type}")

    collectlocation = CollectLocation.objects.filter(zone=zone_id, type=type_id)
    print(f"lieu de collecte : {collectlocation}")

    return render(request, 'search/search.html', {"garbages":garbages,"selected_garbage":selected_garbage, "type_id": type_id, "collectlocation":collectlocation})
