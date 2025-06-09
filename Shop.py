from Storage import Storage
from Store import Store


class Shop(Store):
    title = "Магазин"

    def __init__(self, items:dict, capacity:int=20):
        super().__init__(items, capacity)


    def is_available_space(self, name, count):

        if not super().is_available_space(name, count):
            return False

        if name not in self.items and self.get_unique_items_count() == 5:
            print(f"В {self.title} недостаточно места, попробуйте что то другое")
            return False
        return True

