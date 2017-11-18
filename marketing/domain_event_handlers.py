from marketing.commands import record_facebook_registration_conversion, record_email_registration_conversion
from . import domain_events
from .models import Conversion, User


def handle_user_registered_with_facebook(event):
    record_facebook_registration_conversion(event.user_id)


def handle_user_registered_with_email(event):
    record_email_registration_conversion(event.user_id)


def handle_facebook_registration_conversion_recorded(event: domain_events.FacebookRegistrationConversionRecorded):
    conversion = Conversion.objects.get(conversion_id=event.conversion_id)
    user = User.objects.get(user_id=conversion.user_id)

    data = {
        'conversion_id': conversion.conversion_id,
        'email': user.email
    }

    # Notify Facebook API of the conversion
