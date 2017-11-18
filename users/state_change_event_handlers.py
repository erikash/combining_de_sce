from . import state_change_events
from .models import User


def handle_user_created_event(event: state_change_events.UserCreated):
    user = User()
    user.apply_user_created(event)


def handle_user_social_network_added(event: state_change_events.UserSocialNetworkAdded):
    user = User.objects.get(user_id=event.user_id)
    user.apply_social_network_added(event)
