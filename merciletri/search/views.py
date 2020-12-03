from django.shortcuts import render
from .models import City, CollectLocation, Zone, Garbage, GarbageType

def search_view(request):
    """
        with a location and an selected object, find the answer
    """


    city_image =""
    type_id = None
    zone_id = None

    cities = City.objects.all()

    zones = Zone.objects.all()

    garbages = Garbage.objects.all()

    # garbagetypes = GarbageType.object.all()

    selected_city = request.POST.get("selected_city", None)
    print (f" ville : {selected_city}")

    for city in cities :
        if selected_city == city.name :
            city_image = city.image.url
            # print(f"{city_image}")
    
    selected_zone = request.POST.get("selected_zone", None)
    print (f"zone : {selected_zone}")

    for zone in zones :
        if selected_zone == zone.name :
            zone_id = zone.id
            print(f"Zone : {zone_id}")


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

    return render(request, 'search/search.html', {"cities":cities,"zones":zones, "garbages":garbages,"city_image":city_image, "selected_zone": selected_zone, "selected_garbage":selected_garbage, "zone_id":zone_id, "type_id": type_id, "collectlocation":collectlocation})
