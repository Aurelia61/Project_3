from django.shortcuts import render
from .models import City, CollectLocation, Zone, Garbage, GarbageType

def search_city(request, city_id=None, zone_id=None):
    """
        get the city
    """

    city_image = ""
    cities = City.objects.all()
    zones = None
    garbages = None
    type_id = None
    selected_garbage = None
    garbage_locations = []
    garbage_loc_day_time = {}
    
    if request.method == "POST":

        if city_id is None and zone_id is None:
            selected_city = request.POST.get("selected_city", None)
            print (f" ville : {selected_city}")

            for city in cities :
                if selected_city == city.name :
                    city_image = city.image.url
                    city_id = city.id
                    break;
                    print(f"city_id : {city_id}")

            zones = Zone.objects.filter(city_id=city_id)
            print(f"toutes les zones de la ville : {zones}")
        
        elif zone_id is None:
            zones = Zone.objects.filter(city_id=city_id)
            print(f"toutes les zones de la ville : {zones}")
            
            selected_zone = request.POST.get("selected_zone", None)
            print (f"zone : {selected_zone}")

            for zone in zones :
                # if zone.city_id == city_id:
                if selected_zone == zone.name :
                    zone_id = zone.id
                    break;
                    print(f"Zone : {zone_id}")

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
                    break;
                    print(f"Type : {type_id}")


            collectlocation = CollectLocation.objects.filter(zone=zone_id)

            day_id = None
            for CurrentLoc in collectlocation:
                # print(f"collectlocation:  {collectlocation}")
                try:
                    # print(f"current loc : {CurrentLoc}")
                    GarbageLoc = CurrentLoc.type.get(id=type_id)
                    # print(f"GarbageLoc : {GarbageLoc}")
                    try:
                        day_loc = CurrentLoc.day.get()
                        time_loc = CurrentLoc.time.get()
                        # print(f"jour de col : {day_loc}")
                        garbage_locations.append(f"Pour ce déchet, la collecte se fait {CurrentLoc.name} le {day_loc} {time_loc}")
                        # print(f"current loc name : {CurrentLoc.name}")
                        # print(f"loc id : {CurrentLoc.id}")
                        # print(f" garbage locationS : {garbage_locations}")

                    # garbage_loc_day_time["name"] = CurrentLoc.name
                    # garbage_loc_day_time["when"]["day"] = CurrentLoc.day
                    # garbage_loc_day_time["when"]["time"] = CurrentLoc.time
                    except:
                        # print("NON 1")
                        #todo faire un code spécifiques pour les horaires des décheteries
                        pass
                except:
                    # print("NON 2")
                    #todo faire un message si pas de réponse 
                    pass

            # collectlocation = "ICI"
            # print(f"lieu de collecte pour ce déchet : {garbage_locations}")
            

    return render(
        request, 
        'search/search.html', 
        {
            "cities": cities, 
            "city_image": city_image, 
            "city_id": city_id,
            "zones": zones, 
            "zone_id": zone_id,
            "garbages": garbages, 
            "selected_garbage": selected_garbage,
            "garbage_locations": garbage_locations,
            # "garbage_loc_day_time": garbage_loc_day_time
        })


# def search_zone(request, city_id):
#     """
#         get the zone
#     """

#     zone_id = None

#     zones = Zone.objects.all()
#     print(f"toutes les zones : {zones}")
#     selected_zone = request.POST.get("selected_zone", None)
#     print (f"zone : {selected_zone}")


#     for zone in zones :
#         print(f"Id de la ville de la zone : {zone.city_id}")
#         if zone.city_id == city_id:
#             if selected_zone == zone.name :
#                 zone_id = zone.id
#                 print(f"Zone : {zone_id}")

#     return render(request, 'search/search.html', {"zones":zones, "selected_zone": selected_zone, "zone_id":zone_id})



# def search_garbage(request, city_id, zone_id):
#     """
#         get the garbage type
#     """

#     type_id = None

#     garbages = Garbage.objects.all()

#     # garbagetypes = GarbageType.object.all()

#     selected_garbage = request.POST.get("selected_garbage", None)
#     print (f"déchet : {selected_garbage}")

#     for garbage in garbages :
#         if selected_garbage == garbage.name :
#             type_id = garbage.garbagetype_id
#             print(f"Type : {type_id}")

#     # type = GarbageType.objects.filter(name = selected_garbage)
#     # print(f"type : {type}")

#     collectlocation = CollectLocation.objects.filter(zone=zone_id, type=type_id)
#     print(f"lieu de collecte : {collectlocation}")

#     return render(request, 'search/search.html', {"garbages":garbages,"selected_garbage":selected_garbage, "type_id": type_id, "collectlocation":collectlocation})
