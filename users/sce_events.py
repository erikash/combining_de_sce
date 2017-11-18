class UserCreated(object):
    def __init__(self, user_id, email, hashed_password) -> None:
        self.user_id = user_id
        self.email = email
        self.hashed_password = hashed_password
