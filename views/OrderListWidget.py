from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, \
    QLineEdit, QSizePolicy, QGridLayout, QTabBar, QFrame, QTextEdit
from models.itemModel import ItemModel
from models.OrdersClass import *
from controllers.CartController import CartController
from datetime import datetime


class OrderListWidget(QWidget):

    def __init__(self, itemModel: ItemModel):
        super().__init__()

        self.item_model = itemModel
        self.cart_controller = CartController(itemModel)
        self.setWindowTitle("Order Layout")
        self.cart_controller.checkout_signal.connect(self.update_orders)

        main_layout = QHBoxLayout()

        # Scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Container widget for the orders
        self.orders_container = QWidget()
        self.orders_layout = QHBoxLayout(self.orders_container)
        self.orders_container.setLayout(self.orders_layout)

        scroll_area.setWidget(self.orders_container)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

    def update_orders(self):
        # Clear the orders
        for i in reversed(range(self.orders_layout.count())):
            self.orders_layout.itemAt(i).widget().setParent(None)

        # Add the new orders
        for order in orders_list:
            if isinstance(order, ReadyOrder):
                continue
            order_widget = OrderWidget(order.order_id, order.ingredients, order.order_date)
            self.orders_layout.addWidget(order_widget)


class OrderWidget(QWidget):

    def __init__(self, order_number, ingredients, order_datetime: datetime):
        super().__init__()
        self.order_number = order_number
        self.setFixedSize(375, 500)

        layout = QVBoxLayout()

        # Order number
        self.order_number_label = QLabel(str(order_number))
        self.order_number_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.order_number_label)

        # Ingredients
        ingredients_layout = QVBoxLayout()
        ingredients_label = QLabel("Ingredients:")
        self.ingredients_text = QTextEdit(ingredients)
        self.ingredients_text.setReadOnly(True)
        self.ingredients_text.setFontPointSize(18)

        ingredients_layout.addWidget(ingredients_label)
        ingredients_layout.addWidget(self.ingredients_text)

        ingredients_frame = QFrame()
        ingredients_frame.setFrameShape(QFrame.Box)
        ingredients_frame.setLayout(ingredients_layout)
        layout.addWidget(ingredients_frame)

        # Bottom section
        bottom_layout = QHBoxLayout()
        self.order_datetime_label = QLabel(f"Ordered: {order_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
        self.ready_button = QPushButton("Ready")
        self.ready_button.clicked.connect(self.ready_button_clicked)
        self.ready_button.setFixedWidth(100)

        bottom_layout.addWidget(self.order_datetime_label)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.ready_button)

        bottom_frame = QFrame()
        bottom_frame.setFrameShape(QFrame.Box)
        bottom_frame.setLayout(bottom_layout)
        layout.addWidget(bottom_frame)

        self.setLayout(layout)

    def ready_button_clicked(self):
        make_order_ready(self.order_number)
        self.deleteLater()
