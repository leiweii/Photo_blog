from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    
    profile_photo = models.ImageField(verbose_name='Photo de profil', upload_to='profile_photos/')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit',
# Le premier argument de ManyToManyField est le modèle avec lequel vous créez une relation, 
# ici 'self' pour le modèle User. Utilisez limit_choices_to pour restreindre les utilisateurs 
# suivis aux rôles spécifiques, comme CREATOR. Spécifiez symmetrical=False pour indiquer que la 
# relation n'est pas symétrique, nécessaire seulement lorsque les deux modèles sont identiques.
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)
