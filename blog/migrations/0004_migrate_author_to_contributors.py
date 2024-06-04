# Generated by Django 5.0.6 on 2024-06-03 14:28

from django.db import migrations

def migrate_author_to_contributors(apps, schema_editor):
    Blog = apps.get_model('blog', 'Blog')
    for blog in Blog.objects.all():
        if blog.author:
            blog.contributors.add(
                blog.author, through_defaults={'contribution': 'Auteur principal'})


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_author_blogcontributor_blog_contributors'),
    ]

    operations = [
        migrations.RunPython(migrate_author_to_contributors)
    ]
