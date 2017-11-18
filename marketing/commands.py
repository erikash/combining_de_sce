from marketing.models import Conversion
from pubsub import PersistentPubSub


def record_email_registration_conversion(user_id):
    events = Conversion.record_email_registration_conversion(user_id=user_id, source=Conversion.SOURCE_EMAIL)

    PersistentPubSub.publish(events)


def record_facebook_registration_conversion(user_id):
    events = Conversion.record_facebook_registration_conversion(user_id=user_id, source=Conversion.SOURCE_FB)

    PersistentPubSub.publish(events)
