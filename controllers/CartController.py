from PySide6.QtCore import QObject, Signal
from models.itemModel import ItemModel
from views.CartItemButton import CartItemButton
from models.OrderModel import OrderModel


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
        self.orderModel = OrderModel(itemModel.db)
        CartController._initialized = True

        self.total_price = 0
        self.checkout_dict: dict = {}

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

    def get_total_price(self, layout) -> float:
        self.total_price = 0
        self.checkout_dict = {}

        for i in range(layout.count()):
            item = layout.itemAt(i).widget()
            if isinstance(item, CartItemButton):
                self.total_price += item.price * item.number
                if len(item) < 100:  # FIXME I use the __len__ method to check if the name length is less than 100 to put it to db
                    self.checkout_dict[str(item)] = item.number
        return self.total_price

    def checkout_to_db(self) -> None:
        checkout_dict = dict(sorted(self.checkout_dict.items()))  # сортування за ключем
        items_string: str = ', '.join([f"{key} x{value}" for key, value in checkout_dict.items()])
        # calculating profit
        profit = 0
        for item_in_cart, number in self.checkout_dict.items():
            item = self.get_item_by_name(item_in_cart)[0]
            profit += (item[3] - item[4]) * number
        print(f"Profit: {profit}")
        self.orderModel.db.connect()
        self.orderModel.addOrderToDb(self.total_price, profit, items_string)
        self.orderModel.db.disconnect()
        self.clear_cart()
