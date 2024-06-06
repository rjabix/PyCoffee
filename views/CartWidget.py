from PySide6.QtCore import Slot
from PySide6.QtGui import Qt, QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea
from models.itemModel import ItemModel
from models.OrderModel import OrderModel
from controllers.CartController import CartController
from views.CartItemButton import CartItemButton


class CartWidget(QWidget):
    def __init__(self, itemModel: ItemModel, orderModel: OrderModel):
        super().__init__()

        self.itemModel = itemModel
        self.orderModel = orderModel

        self.cartController = CartController(itemModel)
        self.cartController.cart_changed.connect(self.update_widget)

        with open("assets/menuwindow_style.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.setWindowTitle("Koszyk")

        # with open("assets/cartwindow_style.qss", "r") as f:
        #    self.setStyleSheet(f.read())

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        font = QFont()
        font.setFamily("EB Garamond")
        font.setPointSize(25)

        label = QLabel("Koszyk")
        label.setFont(font)
        self.layout.addWidget(label)
        label.setAlignment(Qt.AlignCenter)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        # Create a new widget for the scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_widget.setLayout(scroll_layout)
        self.scroll_area.setWidget(scroll_widget)

        self.total_price_label = QLabel(f"Suma: 0 zł")
        self.total_price_label.setFont(font)
        self.layout.addWidget(self.total_price_label)

        checkout_button = QPushButton("Zapłacić")
        checkout_button.setFont(font)
        checkout_button.setObjectName("menu_item_button")
        checkout_button.setFixedHeight(50)
        checkout_button.clicked.connect(self.checkout_button_clicked)
        self.layout.addWidget(checkout_button)

    def clear_cart_layout(self):
        layout = self.scroll_area.widget().layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    @Slot()
    def update_widget(self):
        self.clear_cart_layout()
        for item in self.cartController.cart_list:
            found_item = self.cartController.get_item_by_name(item)
            pickedButton = CartItemButton(found_item[0][2], found_item[0][3], found_item[0][5])
            pickedButton.number_changed.connect(self.update_total_price)
            pickedButton.setObjectName("cart_item_button")
            self.scroll_area.widget().layout().addWidget(pickedButton)
        self.update_total_price()

    @Slot()
    def update_total_price(self):
        self.total_price_label.setText(f"Suma: \
        {self.cartController.get_total_price(self.scroll_area.widget().layout())} zł")

    def checkout_button_clicked(self):
        if not self.cartController.cart_list:
            return
        self.cartController.checkout_to_db()
        self.update_widget()

