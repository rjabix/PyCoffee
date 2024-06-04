from views.CartWidget import CartWidget
from views.EditMenuWidget import EditMenuWidget
from views.MenuWidget import MenuWidget
from models.itemModel import ItemModel
from models.OrderModel import OrderModel
from controllers.CartController import CartController
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QPushButton, )


class MainWindow(QMainWindow):
    def __init__(self, itemModel: ItemModel, orderModel: OrderModel):
        super().__init__()

        self.itemModel = itemModel
        self.orderModel = orderModel

        self.setWindowTitle("Kawiarnia PyCoffee")
        self.setFixedHeight(600)
        self.setFixedWidth(1000)

        with open("assets/mainwindow_style.qss", "r") as f:
            self.setStyleSheet(f.read())

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        self.stacked_widget = QStackedWidget()

        main_menu = QWidget()
        main_menu.setObjectName("main_menu")
        main_menu_layout = QHBoxLayout()

        # Tworzenie przycisków
        order_button = QPushButton("Złożyć zamówienie")
        order_button.setObjectName("main_menu_button")
        order_button.setFont(QFont("Georgia", 20))
        main_menu_layout.addWidget(order_button)

        storage_button = QPushButton("Zmienić produkty \nw menu")
        storage_button.setObjectName("main_menu_button")
        storage_button.setFont(QFont("Georgia", 20))
        main_menu_layout.addWidget(storage_button)

        report_button = QPushButton("Historia zamówień \noraz statystyka")
        report_button.setObjectName("main_menu_button")
        report_button.setFont(QFont("Georgia", 20))
        main_menu_layout.addWidget(report_button)

        main_menu.setLayout(main_menu_layout)

        # Tworzenie stron
        menu_page = MenuWidget(itemModel)
        edit_page = EditMenuWidget(itemModel)
        cart_page = CartWidget(self.itemModel, self.orderModel)

        # Додавання сторінок до stacked_widget
        self.stacked_widget.addWidget(main_menu)
        self.stacked_widget.addWidget(menu_page)
        self.stacked_widget.addWidget(edit_page)
        # self.stacked_widget.addWidget(report_page)
        self.stacked_widget.addWidget(cart_page)

        layout.addWidget(self.stacked_widget)
        main_widget.setLayout(layout)

        # Підключення кнопок до сторінок
        order_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(menu_page))
        storage_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(edit_page))
        # report_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(report_page))
        # search_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(search_page))

        # Створення меню
        menubar = self.menuBar()

        # Створення меню "Файл"
        file_menu = menubar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu("Window")

        main_action = QAction("Główna", self)
        main_action.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(main_menu))
        order_action = QAction("Złożyć zamówienie", self)
        order_action.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(menu_page))
        storage_action = QAction("Zmienić produkty w menu", self)
        storage_action.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(edit_page))
        report_action = QAction("Statystyka", self)
        report_action.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(report_page))

        edit_menu.addAction(main_action)
        edit_menu.addAction(order_action)
        edit_menu.addAction(storage_action)
        edit_menu.addAction(report_action)

        cart_menu = menubar.addMenu("Koszyk")

        cart_action = QAction("Koszyk", self)
        cart_action.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(cart_page))
        clear_action = QAction("Wyczyść koszyk", self)
        clear_action.triggered.connect(lambda: CartController.clear_cart())

        cart_menu.addAction(cart_action)
        cart_menu.addAction(clear_action)
