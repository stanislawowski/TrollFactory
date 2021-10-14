class UnmetDependenciesException(Exception):
    def __init__(self, message):
        self.message = message


class UnsupportedDatasetException(Exception):
    def __init__(self, message):
        self.message = message


class InvalidGenderException(Exception):
    def __init__(self, message):
        self.message = message
