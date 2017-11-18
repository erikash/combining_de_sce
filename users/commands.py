from pubsub import PersistentPubSub
from users.models import User


def register_user_with_email(email, password):
    events = User.register_user_with_email(email, password)

    PersistentPubSub.publish(events)


def register_user_with_facebook(fb_email, fb_token):
    events = User.register_user_with_facebook(fb_email, fb_token)

    PersistentPubSub.publish(events)
