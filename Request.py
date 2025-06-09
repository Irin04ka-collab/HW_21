from Shop import Shop
from Store import Store


class Request:
    def __init__(self, user_string, store:Store, shop:Shop):
        if len(user_string.split()) != 7 or user_string.split()[0] != "Доставить":
            raise ValueError("Не верный формат запроса")
        self.from_ = user_string.split()[4]
        self.to_ = user_string.split()[6]
        self.amount = int(user_string.split()[1])
        self.product = user_string.split()[2]
        self.store = store
        self.shop = shop

    def check_avalable(self):
        if self.from_ == "склад":
            if self.store.is_available_items(self.product, self.amount) and self.shop.is_available_space(self.product, self.amount):
                print("Нужное количество есть на складе")
                self.store.remove(self.product, self.amount)
                self.shop.add(self.product, self.amount)
                self._print_logistic()
                return True

        if self.from_ == "магазин":
            if self.shop.is_available_items(self.product, self.amount) and self.store.is_available_space(self.product, self.amount):
                print ("Нужное количество есть на магазине")
                self.shop.remove(self.product, self.amount)
                self.store.add(self.product, self.amount)
                self._print_logistic()
                return True
            
    def _print_logistic(self):
        print(f"Курьер забрал {self.amount} {self.product} со {self.from_}\n"
              f"Курьер везет {self.amount} {self.product} со {self.from_} в {self.to_}\n"
              f"Курьер доставил {self.amount} {self.product} в {self.to_}\n")


