# Generated by Django 5.0.6 on 2025-03-26 20:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_commentaire'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='description',
        ),
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Commentaire')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
    ]
