from django.test import TransactionTestCase

from marketing.models import Conversion
from users.commands import register_user_with_email, register_user_with_facebook
from users.models import User

PASSWORD = "123123"
EMAIL = "erikash@gmail.com"
FB_TOKEN = "testsetsetsetset"


class UserTestCase(TransactionTestCase):
    def test_can_register_user_with_email(self):
        register_user_with_email(EMAIL, PASSWORD)

        user = User.objects.get(email=EMAIL)
        self.assertEquals(user.hashed_password, PASSWORD)
        self.assertEquals(user.source, User.SOURCE_EMAIL)

        conversion = Conversion.objects.get(user_id=user.user_id)
        self.assertEquals(conversion.source, Conversion.SOURCE_EMAIL)

    def test_can_register_user_with_facebook(self):
        register_user_with_facebook(EMAIL, FB_TOKEN)

        user = User.objects.get(email=EMAIL)
        self.assertEquals(user.source, User.SOURCE_FB)
        self.assertEquals(user.fb_token, FB_TOKEN)

        conversion = Conversion.objects.get(user_id=user.user_id)
        self.assertEquals(conversion.source, Conversion.SOURCE_FB)
