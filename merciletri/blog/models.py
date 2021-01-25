from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    """
        
    """

    title = models.CharField(
        "titre", 
        max_length = 80
        )

    body = RichTextField(blank=True, null=True)

    pickup_line = models.CharField(
        "phrase d'accroche",
        max_length = 150,
        default=""
    )
    
    def __str__(self):
        """
            overload the print

        """
        
        # change the name of the article by his title on admin page (without it should be named "Article object (n)")
        return self.title
