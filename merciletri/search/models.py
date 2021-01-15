from django.db import models
from django.db.models.fields import Field


class City(models.Model):
    """
        manage the City class
    """

    name = models.CharField(
        "Nom de la ville",
        max_length = 100
    )

    image = models.ImageField(
        "Image",
        upload_to = "",
        blank = True
    )


    def __str__(self):
        """
            
        """

        return f"{self.name}"


    class Meta:
        """
            
        """

        verbose_name = "Ville"
        verbose_name_plural = "Villes"
        ordering = ["name"]

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


    def __str__(self):
        """
            
        """

        return f"{self.name}"


    class Meta:
        """
            
        """

        verbose_name = "Zone"
        verbose_name_plural = "Zones"
        ordering = ["name"]

class GarbageType(models.Model):
    """
        manage the Garbage Type class
    """

    name = models.CharField(
        "Type de déchet",
        max_length = 100
    )

    def __str__(self):
        """
            
        """

        return f"{self.name}"


    class Meta:
        """
            
        """

        verbose_name = "Type de déchet"
        verbose_name_plural = "Types de déchet"
        ordering = ["name"]

class Garbage(models.Model):
    """
        manage the Garbage class
    """

    name = models.CharField(
        "Nom du déchet",
        max_length = 100
    )

    image = models.ImageField(
        "Image",
        upload_to = "",
        blank = True
    )

    destination = models.CharField(
        "Destination",
        max_length = 60,
        null = False,
        default = "Poubelle d'ordures ménagères"
    )

    garbagetype = models.ForeignKey(
        GarbageType,
        # if a type is deleted, all the dependant garbages will be kept
        on_delete = models.PROTECT,   
    )

    def __str__(self):
        """
            
        """

        return f"{self.name}"


    class Meta:
        """
            
        """

        verbose_name = "Déchet"
        verbose_name_plural = "Déchets"
        ordering = ["name"]

class Time(models.Model):
    """
        manage the Time class
    """

    collecttime = models.CharField(   #! charfield car on note l'heure en texte ?
        "Heure de collecte",
        max_length = 100,
        blank = True
    )

    wintertime = models.CharField(   #! charfield car on note l'heure en texte ?
        "Heure d'hiver",
        max_length = 100,
        blank = True
    )

    summertime = models.CharField(   #! charfield car on note l'heure en texte ?
        "Heure d'été'",
        max_length = 100,
        blank = True
    )

    def __str__(self):
        """
            
        """

        if self.collecttime:
            time = self.collecttime
        elif self.wintertime:
            time = self.wintertime + " (du 2 nomembre au 14 mars)"
        else:
            time = self.summertime + " (du 15 mars au 31 octobre)"
        
        return f"{time}"


    class Meta:
        """
            
        """

        verbose_name = "Horaire"
        verbose_name_plural = "Horaires"
        ordering = ["collecttime"]

class Day(models.Model):
    """
        manage the Day class
    """

    nameday = models.CharField(
        "Jour",
        max_length = 50
    )

    def __str__(self):
        """
            
        """

        return f"{self.nameday}"


    class Meta:
        """
            
        """

        verbose_name = "Jour"
        verbose_name_plural = "Jours"
        ordering = ["nameday"]

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

    time = models.ManyToManyField(
        Time
    )

    type = models.ManyToManyField(
        GarbageType
    )

    def __str__(self):
        """
            
        """

        return f"{self.name}"


    class Meta:
        """
        """

        verbose_name = "Lieu de collecte"
        verbose_name_plural = "Lieux de collecte"
        ordering = ["name"]
