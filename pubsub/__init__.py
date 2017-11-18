# Could be Kafka or EventStore or another persistent event store with pubsub capabilities
class PersistentPubSub(object):
    @classmethod
    def publish(cls, events):
        from users import state_change_event_handlers as users_state_change_event_handlers
        from users import domain_event_handlers as users_domain_event_handlers
        from marketing import state_change_event_handlers as marketing_state_change_event_handlers
        from marketing import domain_event_handlers as marketing_domain_event_handlers

        # This should be implemented convention based.. this is demo code :)
        STATE_CHANGE_SUBSCRIBER_MAP = {
            'UserCreated': [
                users_state_change_event_handlers.handle_user_created_event,
                marketing_state_change_event_handlers.handle_user_created_event],
            'UserSocialNetworkAdded': [users_state_change_event_handlers.handle_user_social_network_added],

            'ConversionCreated': [marketing_state_change_event_handlers.handle_conversion_created]
        }

        DOMAIN_EVENT_SUBSCRIBER_MAP = {
            'UserRegisteredWithEmail': [users_domain_event_handlers.handle_user_registered_with_email,
                                        marketing_domain_event_handlers.handle_user_registered_with_email],
            'UserRegisteredWithFB': [marketing_domain_event_handlers.handle_user_registered_with_facebook],

            'FacebookRegistrationConversionRecorded': [
                marketing_domain_event_handlers.handle_facebook_registration_conversion_recorded]
        }

        SUBSCRIBER_MAP = dict(STATE_CHANGE_SUBSCRIBER_MAP, **DOMAIN_EVENT_SUBSCRIBER_MAP)

        for event in events:
            event_class_name = event.__class__.__name__

            if event_class_name not in SUBSCRIBER_MAP:
                continue

            [handler(event) for handler in SUBSCRIBER_MAP[event_class_name]]
