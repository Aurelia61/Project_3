from django.db import models

class Article(models.Model):
    """

    """

    title = models.CharField(
        "titre", 
        max_length = 80
        )

    body = models.TextField(
        "contenu"
    )
    
    pickup_line = models.CharField(
        "phrase d'accroche",
        max_length = 150,
        default=""
    )

    #todo ajouter : lien externe, date, auteur, catégorie, image (une ou pl ?)

    
    def __str__(self):
        """
            overload the print

        """
        
        # change the name of the article by his title on admin page (without it should be named "Article object (n)")
        return self.title