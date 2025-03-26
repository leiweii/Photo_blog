from django.test import TestCase
from .models import User

# Create your tests here.
class AuthenticationTest(TestCase):
    def test_create_user(self):
        def setUp(self):
            self.user = User.objects.create_user(
                username='test',
                email='test@test.com',
                password='test'
            )

        def test_create_user(self):
            self.assertEqual(self.user.email, 'test@test.com')
            self.assertEqual(self.user.username, 'test')