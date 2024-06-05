from PySide6.QtCore import QObject, Signal


class CartController(QObject):
    _instance = None
    _initialized = False
    cart_changed = Signal()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CartController, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if CartController._initialized:
            return
        super().__init__()
        self.cart_list = []
        CartController._initialized = True

    def add(self, product):
        if product not in self.cart_list:
            self.cart_list.append(product)
            self.cart_changed.emit()
        else:
            raise Exception("Produkt już jest w koszyku :)")

    def remove(self, product):
        self.cart_list.remove(product)
        self.cart_changed.emit()

    def clear_cart(self):
        self.cart_list = []
        print("Koszyk wyczyszczony")
        self.cart_changed.emit()
