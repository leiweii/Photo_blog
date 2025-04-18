from django.conf import settings
from django.db import models
from PIL import Image
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Categorie(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nom de la catégorie')

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(verbose_name='image')
    caption = models.CharField(max_length=128, blank=True, verbose_name='légende')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categorie, related_name='photos', blank=True, verbose_name="Catégories")
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return f'{self.caption}'


class Blog(models.Model):
    photo = models.ForeignKey('Photo', null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128, verbose_name='titre')
    content = models.CharField(max_length=5000, verbose_name='contenu')
    categories = models.ManyToManyField(Categorie, related_name='blogs', blank=True, verbose_name="Catégories")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs') 
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    word_count = models.IntegerField(null=True)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BlogContributor', related_name='contributions')

    def _get_word_count(self):
        return len(self.content.split(' '))

    def save(self, *args, **kwargs):
        self.word_count = self._get_word_count()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class BlogContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)
    
    class Meta:
        unique_together = ('contributor', 'blog')



class Commentaire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    text = models.TextField("Commentaire")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.user} sur {self.content_object}"