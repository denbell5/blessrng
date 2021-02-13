class RandomIntDto:
    def __init__(self, floor, ceiling, value):
        self.floor = floor
        self.ceiling = ceiling
        self.value = value


class RandomPasswordDto:
    def __init__(self, length, password):
        self.length = length
        self.password = password