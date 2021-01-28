from django.shortcuts import render
from .models import City, CollectLocation, Zone, Garbage, GarbageType

def search_city(request, city_id=None, zone_id=None, city_name=None, zone_name=None, garbage_name=None):
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

            for city in cities :
                if selected_city == city.name :
                    city_image = city.image.url
                    city_id = city.id
                    city_name = city.name
                    break;

            zones = Zone.objects.filter(city_id=city_id)
        
        elif zone_id is None:
            zones = Zone.objects.filter(city_id=city_id)
            selected_zone = request.POST.get("selected_zone", None)

            for zone in zones :
                if selected_zone == zone.name :
                    zone_id = zone.id
                    zone_name = zone.name
                    break;

            garbages = Garbage.objects.all()

        else:
            garbages = Garbage.objects.all()
            
            selected_garbage = request.POST.get("selected_garbage", None)

            type_id = None

            for garbage in garbages :
                selected_garbage_without_spaces =(selected_garbage).join("")
                garbage_name_without_spaces = (garbage.name).join("")
                if selected_garbage_without_spaces == garbage_name_without_spaces :
                    type_id = garbage.garbagetype_id
                    garbage_name = garbage.name
                    break;

            collectlocation = CollectLocation.objects.filter(zone=zone_id)

            for CurrentLoc in collectlocation:
                try:
                    garbage_loc = CurrentLoc.type.get(id=type_id)
                    try:
                        day_loc = CurrentLoc.day.get()
                        time_loc = CurrentLoc.time.get()
                        garbage_locations.append(f"Pour ce déchet, la collecte se fait {CurrentLoc.name} le {day_loc} {time_loc}")
                    except:
                        #todo faire un code spécifiques pour les horaires des décheteries
                        pass
                except:
                    #todo faire un message si pas de réponse 
                    pass

    return render(
        request, 
        'search/search.html', 
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
        }
    )
