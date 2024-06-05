from PySide6.QtCore import QObject, Signal
from models.itemModel import ItemModel
from views.CartItemButton import CartItemButton

class CartController(QObject):  # singleton
    _instance = None
    _initialized = False
    cart_changed = Signal()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CartController, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, itemModel: ItemModel):
        if CartController._initialized:
            return
        super().__init__()
        self.itemModel = itemModel
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

    def get_item_by_name(self, name):
        self.itemModel.db.connect()
        data = self.itemModel.getItems(name=name)
        self.itemModel.db.disconnect()
        return data

    def clear_cart(self):
        self.cart_list = []
        print("Koszyk wyczyszczony")
        self.cart_changed.emit()

    @staticmethod
    def get_total_price(layout) -> float:
        total_price = 0
        for i in range(layout.count()):
            item = layout.itemAt(i).widget()
            if isinstance(item, CartItemButton):
                total_price += item.price * item.number
        return total_price

    def checkout(self):
        print("Zapłacono")
        self.clear_cart()
