from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from models.itemModel import ItemModel
from models.OrderModel import OrderModel
from controllers.CartController import CartController


class CartWidget(QWidget):
    def __init__(self, itemModel: ItemModel, orderModel: OrderModel):
        super().__init__()

        self.itemModel = itemModel
        self.orderModel = orderModel

        self.cartController = CartController()

        self.setWindowTitle("Koszyk")

        #with open("assets/cartwindow_style.qss", "r") as f:
        #    self.setStyleSheet(f.read())

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Koszyk")
        layout.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)

        self.cart_items = []

        self.total_price = 0

        self.total_price_label = QLabel(f"Suma: {self.total_price} zł")
        layout.addWidget(self.total_price_label)

        self.checkout_button = QPushButton("Zapłacić")
        layout.addWidget(self.checkout_button)

    def add_item(self, item):
        self.cart_items.append(item)
        self.total_price += item[1]
        self.total_price_label.setText(f"Suma: {self.total_price} zł")

    def remove_item(self, item):
        self.cart_items.remove(item)
        self.total_price -= item[1]
        self.total_price_label.setText(f"Suma: {self.total_price} zł")

    @classmethod #треба було так зробити, щоб мати змогу у карт_контролері викликати цей метод
    def update_widget_cls(cls):
        print("Updating cart widget cls")
        cls.update_widget_self()

    def update_widget_self(self):
        print("Updating cart widget self")

