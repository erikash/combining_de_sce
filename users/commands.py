from users.domain_event_handlers import UserRegisteredWithEmailHandler
from users.models import User


class RegisterUserWithEmail(object):
    def __init__(self, email, password) -> None:
        super().__init__()

        self.email = email
        self.password = password

    def execute(self):
        user = User()  # Don't mess with Django ORM
        events = user.register_user_with_email(self.email, self.password)

        # Demo code this should be convention based by class name
        user.apply_user_created(events[0])
        UserRegisteredWithEmailHandler().handle(events[1])


