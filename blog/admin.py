from django.contrib import admin
from .models import Photo, Blog, BlogContributor

admin.site.register(Photo)
admin.site.register(Blog)
admin.site.register(BlogContributor)