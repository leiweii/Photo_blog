from django.contrib import admin
from .models import Photo, Blog, BlogContributor, Categorie

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image',  'uploader', 'date_created')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'starred', 'word_count')

class CustomBlogContributorAdmin(admin.ModelAdmin):
    list_display = ('contributor', 'blog', 'contribution')



admin.site.register(BlogContributor, CustomBlogContributorAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Blog, BlogAdmin)


admin.site.register(Categorie)