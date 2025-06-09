from Request import Request
from Shop import Shop
from Store import Store

dict_of_store = {"печеньки":30, "коробки":50, "собачки":13, "цветочки":2} #95
dict_of_shop = {"печеньки":1, "ящики":5, "ужи":13} #19

print("Добрый день! Это программа обсуживающая логистику склада\n"
      "Для осуществления перемещения товара необходимо сформиро-\n"
      "вать запрос по следующему шаблону:\n"
      "Доставить 3 печеньки из склад в магазин\n")

store = Store(dict_of_store)
shop = Shop(dict_of_shop)

print("В склад хранится:\n")
store.get_items()
print("\nВ магазин хранится:\n")
shop.get_items()

while True:
    string_of_user = input(f"\nВведите ваш запрос:\n")
    if string_of_user.lower() == "стоп":
        break

    try:
        request = Request(string_of_user, store, shop)
        request.check_avalable()

        print("В склад хранится:\n")
        store.get_items()
        print("\nВ магазин хранится:\n")
        shop.get_items()

    except ValueError as e:
        print(e)
        print("Корретный формат: Доставить 3 печеньки из склад в магазин\n")

