from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, \
    QLineEdit, QSizePolicy, QGridLayout
from views.MenuItemButton import MenuItemButton
from models.itemModel import ItemModel
from controllers.MenuController import MenuController


class MenuWidget(QWidget):
    def __init__(self, itemModel: ItemModel):
        super().__init__()
        self.itemModel = itemModel

        self.TypeDictionary = {
            "Napój": 0,
            "Jedzenie": 1,
            "Deser": 2,
            "Inne": 3
        }

        self.setWindowTitle("Menu")

        with open("assets/menuwindow_style.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.tab_widget = QTabWidget()

        self.beverages_tab = self.create_tab("Napój")
        self.food_tab = self.create_tab("Jedzenie")
        self.dessert_tab = self.create_tab("Deser")
        self.other_tab = self.create_tab("Inne")

        # Add tabs to the tab widget
        self.tab_widget.addTab(self.beverages_tab, "Napoje")
        self.tab_widget.addTab(self.food_tab, "Jedzenie")
        self.tab_widget.addTab(self.dessert_tab, "Desery")
        self.tab_widget.addTab(self.other_tab, "Inne")

        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def create_tab(self, tab_name):
        menuController = MenuController(self.itemModel)
        items = menuController.get_items_by_type(self.TypeDictionary[tab_name])
        # Create a scrollable area for the tab content
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a grid layout for the tab content
        grid_layout = QGridLayout()
        content_widget = QWidget()
        content_widget.setLayout(grid_layout)

        # Add menu items as buttons to the grid layout
        items_per_row = 3

        for index, (id, type, name, price, cost, image_path) in enumerate(items):
            menu_item_button = MenuItemButton(name, price, image_path)
            menu_item_button.setObjectName("menu_item_button")
            menu_item_button.clicked.connect(self.item_button_clicked)

            # Calculate the row and column index
            row = index // items_per_row
            col = index % items_per_row

            grid_layout.addWidget(menu_item_button, row, col)

        scroll_area.setWidget(content_widget)

        # Return the scrollable area as the tab widget
        return scroll_area

    def item_button_clicked(self):
        button = self.sender()
        print(f"Button clicked: {str(button)}")
        menuController = MenuController(self.itemModel)
        menuController.add_item_to_cart(str(button))

