import uuid

from django.db import models
from django.db.models import Model

from . import sce_events
from . import domain_events


class User(Model):
    user_id = models.UUIDField(primary_key=True)
    email = models.CharField(max_length=255, null=True, blank=False)

    def register_user_with_email(self, email, password):
        user_id = uuid.uuid4()
        hashed_password = password  # Demo code sue me

        user_created = sce_events.UserCreated(user_id=str(user_id),
                                              email=email,
                                              hashed_password=hashed_password)

        user_registered_with_email = domain_events.UserRegisteredWithEmail(user_id=str(user_id))

        return [user_created, user_registered_with_email]

    def apply_user_created(self, event: sce_events.UserCreated):
        self.user_id = uuid.UUID(event.user_id)
        self.email = event.email
        self.hashed_password = event.hashed_password
        self.save()
