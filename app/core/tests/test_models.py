from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email successfully"""
        email = 'wotg.ltd@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email is lowercase"""
        email = 'test@LONDON.COM'
        user = get_user_model().objects.create_user(email, 'qqq123')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """test Django superuser creation"""
        user = get_user_model().objects\
            .create_superuser('test@qqq.com', 'qqq123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
