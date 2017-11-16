from django.db import models
from django.core.validators import FileExtensionValidator

class Article(models.Model):
    pseudo = models.CharField(max_length=42)
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution",
                                auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Article publié ?",
                                     default=True)
    categorie = models.ForeignKey('Categorie')
    photo = models.ImageField(upload_to='crepes/staticfiles/photos/', validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])],blank=True)

    """ méthodes pour recuperer tous les commentaires visibles """
    def comment_list(self):
        commentaires = self.comment_set.filter(is_visible=True).order_by('-date')
        return commentaires

    def __str__(self):
        return self.titre

    # En cas de besoin, vous êtes autorisé à rajouter des méthodes ou
    # propriétés dans ce modèle.


class Categorie(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    pseudo = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de création",
                                auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="commentaire visible ?",
                                     default=True)
    article = models.ForeignKey('Article', default=1)

    def __str__(self):
        return self.pseudo
