from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items:dict, capacity:int):
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
