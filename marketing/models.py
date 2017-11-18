import uuid

from django.db import models

from . import domain_events
from . import state_change_events


class User(models.Model):
    user_id = models.UUIDField(primary_key=True)
    email = models.CharField(max_length=255, null=False, blank=False)

    def apply_user_created(self, event):
        self.user_id = event.user_id
        self.email = event.email
        self.save()


class Conversion(models.Model):
    SOURCE_EMAIL = 'EMAIL'
    SOURCE_FB = 'FB'

    SOURCE_CHOICES = (
        (SOURCE_FB, 'Facebook'),
        (SOURCE_EMAIL, 'EMAIL')
    )

    conversion_id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField()
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, null=False, blank=False)

    @staticmethod
    def record_email_registration_conversion(user_id, source):
        conversion_id = Conversion._generate_conversion_id()

        return [
            state_change_events.ConversionCreated(conversion_id=conversion_id,
                                                  user_id=user_id,
                                                  source=source),
            domain_events.EmailRegistrationConversionRecorded(conversion_id=conversion_id)
        ]

    @staticmethod
    def record_facebook_registration_conversion(user_id, source):
        conversion_id = Conversion._generate_conversion_id()

        return [
            state_change_events.ConversionCreated(conversion_id=conversion_id,
                                                  user_id=user_id,
                                                  source=source),
            domain_events.FacebookRegistrationConversionRecorded(conversion_id=conversion_id)
        ]

    def apply_conversion_recorded(self, event: state_change_events.ConversionCreated):
        self.conversion_id = event.conversion_id
        self.user_id = event.user_id
        self.source = event.source
        self.save()

    @staticmethod
    def _generate_conversion_id():
        return uuid.uuid4()
