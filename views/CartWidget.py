from PySide6.QtCore import Slot
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
        self.cartController.cart_changed.connect(self.update_widget)

        self.setWindowTitle("Koszyk")

        #with open("assets/cartwindow_style.qss", "r") as f:
        #    self.setStyleSheet(f.read())

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        label = QLabel("Koszyk")
        self.layout.addWidget(label)
        label.setAlignment(Qt.AlignCenter)

        self.cart_items = []

        self.total_price = 0

        self.total_price_label = QLabel(f"Suma: {self.total_price} zł")
        self.layout.addWidget(self.total_price_label)

        checkout_button = QPushButton("Zapłacić")
        self.layout.addWidget(checkout_button)

    @Slot()
    def update_widget(self):
        self.clear_layout()
        print("Updating cart widget self")
        label = QLabel("update")
        self.layout.addWidget(label)

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

