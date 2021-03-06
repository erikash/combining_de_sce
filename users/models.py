import uuid

from django.db import models
from django.db.models import Model

from . import state_change_events
from . import domain_events


class User(Model):
    SOURCE_EMAIL = 'EMAIL'
    SOURCE_FB = 'FB'

    SOURCE_CHOICES = (
        (SOURCE_FB, 'Facebook'),
        (SOURCE_EMAIL, 'EMAIL')
    )
    user_id = models.UUIDField(primary_key=True)
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, null=False, blank=False)
    email = models.CharField(max_length=255, null=True, blank=False)
    fb_token = models.CharField(max_length=255, null=True, blank=False)
    hashed_password = models.CharField(max_length=255, null=True, blank=False)

    @staticmethod
    def register_user_with_email(email, password):
        user_id = User._generate_user_id()
        hashed_password = password  # Demo code sue me

        return [
            state_change_events.UserCreated(user_id=str(user_id),
                                            email=email,
                                            hashed_password=hashed_password,
                                            source=User.SOURCE_EMAIL),
            domain_events.UserRegisteredWithEmail(user_id=str(user_id))
        ]

    @staticmethod
    def register_user_with_facebook(fb_email, fb_token):
        user_id = User._generate_user_id()

        return [
            state_change_events.UserCreated(user_id=str(user_id),
                                            email=fb_email,
                                            hashed_password=None,
                                            source=User.SOURCE_FB),
            state_change_events.UserSocialNetworkAdded(user_id=user_id,
                                                       network_type=state_change_events.UserSocialNetworkAdded.NETWORK_TYPE_FB,
                                                       token=fb_token),
            domain_events.UserRegisteredWithFB(user_id=str(user_id))
        ]

    def apply_user_created(self, event: state_change_events.UserCreated):
        self.user_id = uuid.UUID(event.user_id)
        self.email = event.email
        self.hashed_password = event.hashed_password
        self.source = event.source
        self.save()

    def apply_social_network_added(self, event):
        if event.network_type == state_change_events.UserSocialNetworkAdded.NETWORK_TYPE_FB:
            self.fb_token = event.token
            self.save()

    @staticmethod
    def _generate_user_id():
        return uuid.uuid4()
