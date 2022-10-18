from cls.storage import Storage


class Shop(Storage):
    def __init__(self, items, capacity=5):
        super().__init__(items, capacity)


    def add(self, name, amount) -> None:
        if self.get_unique_items_count() >= 5:
            raise BaseException

        super().add(name, amount)
