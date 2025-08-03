from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            first_name="De",
            last_name="WeW",
            username="dewew",
            email="dewew@gmail.com",
            discipline="AX",
            user_group=231,
            password="foo"
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.username, "dewew")

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(ValueError):
            User.objects.create_user(
                first_name="De",
                last_name="WeW",
                username="",
                email="dewew@gmail.com",
                discipline="AX",
                user_group=231,
                password="foo"
            )

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            first_name="De",
            last_name="WeW",
            username="dewew",
            email="dewew@gmail.com",
            discipline="AX",
            user_group=231,
            password="foo"
        )
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(admin_user.username, "dewew")

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                first_name="De",
                last_name="WeW",
                username="dewew",
                email="dewew@gmail.com",
                discipline="AX",
                user_group=231,
                password="foo",
                is_superuser=False
            )
