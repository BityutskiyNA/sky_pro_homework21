from cls.storage import Storage


class Store(Storage):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)
