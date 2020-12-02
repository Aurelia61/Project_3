from django.db import models

class City(models.Model):
    """
        manage the City class
    """

    name = models.CharField(
        "Nom de la ville",
        max_length = 100
    )


class Zone(models.Model):
    """
        manage the Zone class
    """

    name = models.CharField(
        "Zone",
        max_length = 100
    )

    city = models.ForeignKey(
        City,
        # if a zone is deleted, all the dependant locations will be kept
        on_delete = models.PROTECT,   
    )

class GarbageType(models.Model):
    """
        manage the Garbage Type class
    """

    name = models.CharField(
        "Type de déchets",
        max_length = 100
    )


class Garbage(models.Model):
    """
        manage the Garbage class
    """

    name = models.CharField(
        "Nom du déchet",
        max_length = 100
    )

    garbagetype = models.ForeignKey(
        GarbageType,
        # if a type is deleted, all the dependant garbages will be kept
        on_delete = models.PROTECT,   
    )

class Time(models.Model):
    """
        manage the Time class
    """

    collecttime = models.CharField(   #! charfield car on note l'heure en texte ?
        "Heure de collecte",
        max_length = 100,
        blank = True
    )

    openingtime = models.CharField(   #! charfield car on note l'heure en texte ?
        "Heure d'ouverture",
        max_length = 100,
        blank = True
    )

    closingtime = models.CharField(   #! charfield car on note l'heure en texte ?
        "Heure de fermeture",
        max_length = 100,
        blank = True
    )

class Day(models.Model):
    """
        manage the Day class
    """

    nameday = models.CharField(
        "Jour",
        max_length = 50
    )

    time = models.ManyToManyField(
        Time
    )

class CollectLocation(models.Model):
    """
        manage the Collect Location class
    """

    name = models.CharField(
        "Lieu de collecte",
        max_length = 150
    )

    zone = models.ForeignKey(
        Zone,
        # if a zone is deleted, all the dependant collect location will be kept
        on_delete = models.PROTECT,   
    )

    day = models.ManyToManyField(
        Day
    )

    type = models.ManyToManyField(
        GarbageType
    )






