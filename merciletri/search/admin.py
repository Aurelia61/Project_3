from django.contrib import admin

from .models import City, Zone, GarbageType, Garbage, Time, Day, CollectLocation

# Register models here
admin.site.register(City)
admin.site.register(Zone)
admin.site.register(GarbageType)
admin.site.register(Garbage)
admin.site.register(Time)
admin.site.register(Day)
admin.site.register(CollectLocation)
