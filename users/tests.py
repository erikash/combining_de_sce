from django.test import TransactionTestCase

from .commands import RegisterUserWithEmail
from .models import User

PASSWORD = "123123"
EMAIL = "erikash@gmail.com"


class UserTestCase(TransactionTestCase):
    def test_can_register_user_with_email(self):
        command = RegisterUserWithEmail(EMAIL, PASSWORD)
        command.execute()

        user = User.objects.get(email=EMAIL)
        self.assertEquals(user.email, EMAIL)
