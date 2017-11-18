from django.test import TransactionTestCase

from .commands import RegisterUserWithEmail, RegisterUserWithFacebook
from .models import User

PASSWORD = "123123"
EMAIL = "erikash@gmail.com"
FB_TOKEN = "testsetsetsetset"


class UserTestCase(TransactionTestCase):
    def test_can_register_user_with_email(self):
        command = RegisterUserWithEmail(EMAIL, PASSWORD)
        command.execute()

        user = User.objects.get(email=EMAIL)
        self.assertEquals(user.hashed_password, PASSWORD)
        self.assertEquals(user.source, User.SOURCE_EMAIL)

    def test_can_register_user_with_facebook(self):
        command = RegisterUserWithFacebook(EMAIL, FB_TOKEN)
        command.execute()

        user = User.objects.get(email=EMAIL)
        self.assertEquals(user.source, User.SOURCE_FB)
        self.assertEquals(user.fb_token, FB_TOKEN)
