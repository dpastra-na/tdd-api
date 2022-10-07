"""
Tests for Django models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test that creating a user with an eamil is successful."""
        email = 'test@example.com'
        password = 'test123pass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test if email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, excepted in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, excepted)