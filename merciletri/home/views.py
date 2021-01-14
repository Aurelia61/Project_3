from django.shortcuts import render
from search.models import City, CollectLocation, Zone, Garbage, GarbageType


def home(request, city_id=None, zone_id=None, city_name=None, zone_name=None, garbage_name=None):
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
    garbage_loc_day_time = {}
    
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
                    zone_name = zone.name
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
                    garbage_name = garbage.name
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
        'home/home.html', 
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
