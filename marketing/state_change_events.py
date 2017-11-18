class ConversionCreated(object):
    def __init__(self, conversion_id, user_id, source) -> None:
        super().__init__()
        self.conversion_id = conversion_id
        self.source = source
        self.user_id = user_id
