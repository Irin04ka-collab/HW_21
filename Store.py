from Storage import Storage


class Store(Storage):
    title = "Склад"

    def __init__(self, items:dict, capacity:int=100):
        super().__init__(items, capacity)


    def is_available_space(self, name, count):
        if self.get_free_space() < count:
            print(f"{self.title}: недостаточно места для добавления {count} шт. '{name}'")
            return False
        return True


    def add(self, name, count):
        if self.is_available_space(name, count):
            self.items[name] = self.items.get(name, 0) + count

    def is_available_items(self, name, count):
        if name not in self.items:
            print(f"Товара {name} нет в {self.title}")
            return False

        if self.items[name] < count:
            print(f"Не хватает в {self.title}, попробуйте заказать меньше")
            return False

        return True


    def remove(self, name, count):
        if self.is_available_items(name, count):
            new_count = self.items[name] - count

            if new_count == 0:
                self.items.pop(name)
            else:
                self.items[name] = new_count

    def get_free_space(self):
        total = sum(self.items.values())
        return self.capacity - total

    def get_items(self):
        for name, count in self.items.items():
            print(f"{count} {name}")

    def get_unique_items_count(self):
        return len(self.items.keys())


