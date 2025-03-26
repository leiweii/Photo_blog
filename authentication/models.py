from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Photographe'),
        (SUBSCRIBER, 'Visiteur'),
    )
    
    profile_photo = models.ImageField(verbose_name='Photo de profil', upload_to='profile_photos/')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit',
    )

    # ✅ Cette méthode doit être DANS la classe
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group, _ = Group.objects.get_or_create(name='créateurs')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group, _ = Group.objects.get_or_create(name='utilisateurs')
            group.user_set.add(self)
