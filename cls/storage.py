from typing import Dict

from cls.absStorage import ABSStorage


class Storage(ABSStorage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, name, amount) -> None:
        if self.get_free_space() < amount:
            raise BaseException

        if name in self._items:
            self._items[name] += amount
        else:
            self._items[name] = amount

    def remove(self, name, amount) -> None:
        if self._items.get(name) is None:
            raise BaseException

        if self._items[name] < amount:
            raise BaseException

        self._items[name] -= amount

        if self._items == 0:
            del self._items[name]

    def get_free_space(self) -> int:
        space = 0
        for x in self._items.values():
            space += x
        return self._capacity - space


    def get_items(self) -> dict:
        return self._items


    def get_unique_items_count(self) -> int:
        return len(self._items.keys())

