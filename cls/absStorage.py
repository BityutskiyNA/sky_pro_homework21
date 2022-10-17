from abc import ABC, abstractmethod


class ABSStorage(ABC):
    @abstractmethod
    def add(self, name, koll) -> None:
        pass

    @abstractmethod
    def remove(self, name, koll) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass

