
import views.CartWidget


class CartController():
    cart_list = []  # statyczna lista

    @classmethod  # classmethod = полустатичний метод, який можна викликати через клас, а не через об'єкт класу
    def add(cls, product):
        if product not in cls.cart_list:
            cls.cart_list.append(product)
            views.CartWidget.CartWidget.update_widget_cls()
        else:
            raise Exception("Produkt już jest w koszyku :)")

    @classmethod
    def remove(cls, product):
        cls.cart_list.remove(product)

    @classmethod
    def checkout(cls):
        ...

    @classmethod
    def clear_cart(cls):
        cls.cart_list = []
        print("Koszyk wyczyszczony")
