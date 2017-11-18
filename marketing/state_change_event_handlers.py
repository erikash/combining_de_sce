from .models import User, Conversion


def handle_user_created_event(event):
    user = User()
    user.apply_user_created(event)


def handle_conversion_created(event):
    conversion = Conversion()
    conversion.apply_conversion_recorded(event)
