from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Photo, Blog, Categorie

User = get_user_model()

class BlogTests(TestCase):
    def setUp(self):
        # Créateur
        self.creator = User.objects.create_user(
            username='photographe',
            password='pass1234',
            role='CREATOR'
        )

        # Abonné
        self.subscriber = User.objects.create_user(
            username='abonne',
            password='pass1234',
            role='SUBSCRIBER'
        )

        # Catégorie
        self.cat = Categorie.objects.create(name="Paysage")

        # Photo du créateur
        self.photo = Photo.objects.create(
            caption='Montagne',
            uploader=self.creator,
            image='test.jpg'  # doit exister en mode test ou mocké
        )
        self.photo.categories.add(self.cat)

        # Blog
        self.blog = Blog.objects.create(
            title="Mon premier blog",
            content="Contenu test",
            photo=self.photo,
            author=self.creator
        )
        self.blog.categories.add(self.cat)
        self.blog.contributors.add(self.creator)

    def test_creator_dashboard_access(self):
        self.client.login(username='photographe', password='pass1234')
        response = self.client.get(reverse('creator_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tableau de bord")

    def test_subscriber_cannot_access_creator_dashboard(self):
        self.client.login(username='abonne', password='pass1234')
        response = self.client.get(reverse('creator_dashboard'))
        self.assertEqual(response.status_code, 403)

    def test_blog_creation(self):
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(self.blog.author, self.creator)

    def test_photo_caption(self):
        self.assertEqual(self.photo.caption, "Montagne")

    def test_blog_association_with_photo(self):
        self.assertEqual(self.blog.photo, self.photo)
        self.assertIn(self.cat, self.blog.categories.all())
