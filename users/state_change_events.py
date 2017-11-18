class UserCreated(object):
    def __init__(self, user_id, email, hashed_password, source) -> None:
        self.source = source
        self.user_id = user_id
        self.email = email
        self.hashed_password = hashed_password


class UserSocialNetworkAdded(object):
    NETWORK_TYPE_FB = "FB"

    def __init__(self, user_id, network_type, token) -> None:
        super().__init__()
        self.user_id = user_id
        self.network_type = network_type
        self.token = token
