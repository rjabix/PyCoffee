from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, \
    QLineEdit, QSizePolicy, QGridLayout, QTabBar
from views.MenuItemButton import MenuItemButton
from models.itemModel import ItemModel
from controllers.MenuController import MenuController


class MenuWidget(QWidget):
    def __init__(self, itemModel: ItemModel):
        super().__init__()
        self.itemModel = itemModel
        self.menuController = MenuController(self.itemModel)

        self.TypeDictionary = {
            "Napój": 0,
            "Jedzenie": 1,
            "Deser": 2,
            "Inne": 3
        }

        self.setWindowTitle("Menu")

        with open("assets/menuwindow_style.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.tab_widget = CustomTabWidget()

        self.beverages_tab = self.create_tab("Napój")
        self.food_tab = self.create_tab("Jedzenie")
        self.dessert_tab = self.create_tab("Deser")
        self.other_tab = self.create_tab("Inne")
        self.search_tab = self.create_search_tab()
        self.search_items("")

        # Add tabs to the tab widget
        self.tab_widget.addTab(self.beverages_tab, "Napoje")
        self.tab_widget.addTab(self.food_tab, "Jedzenie")
        self.tab_widget.addTab(self.dessert_tab, "Desery")
        self.tab_widget.addTab(self.other_tab, "Inne")
        self.tab_widget.addTab(self.search_tab, "Wyszukiwarka")

        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def create_tab(self, tab_name):
        items = self.menuController.get_items_by_type(self.TypeDictionary[tab_name])
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

    def create_search_tab(self):
        search_tab = QWidget()
        search_tab_layout = QVBoxLayout()
        search_tab.setLayout(search_tab_layout)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Wyszukaj produkt za nazwą")
        self.search_input.setAlignment(Qt.AlignCenter)
        self.search_input.textChanged.connect(self.search_items)
        search_tab_layout.addWidget(self.search_input)

        self.search_layout = QVBoxLayout()

        # Create a scrollable area for the search results
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget()
        content_widget.setLayout(self.search_layout)
        scroll_area.setWidget(content_widget)

        search_tab_layout.addWidget(scroll_area)  # Add scroll_area to search_tab_layout instead of self.search_layout

        return search_tab

    def search_items(self, text):
        # Create an instance of MenuController
        menuController = MenuController(self.itemModel)

        # Call getItems method with a wildcard search
        items = menuController.get_items_by_name(text)
        items.sort(key=lambda x: x[1])
        # Clear the search tab
        self.clear_layout(self.search_layout)

        # Add the returned items to the search tab
        for item in items:
            menu_item_button = MenuItemButton(item[2], item[3], item[5])

            font = menu_item_button.font
            font.setPointSize(25)
            menu_item_button.right_vertical_layout.itemAt(1).widget().setFont(font)

            menu_item_button.setObjectName("menu_item_button")
            menu_item_button.clicked.connect(self.item_button_clicked)
            self.search_layout.addWidget(menu_item_button)

        # Update the search layout
        self.search_layout.update()

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def item_button_clicked(self):
        button = self.sender()
        print(f"Button clicked: {str(button)}")
        menuController = MenuController(self.itemModel)
        menuController.add_item_to_cart(str(button))


class CustomTabBar(QTabBar):
    def tabSizeHint(self, index):
        size = super().tabSizeHint(index)
        size.setWidth(120)
        return size


class CustomTabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTabBar(CustomTabBar())

    def tabBar(self):
        tab_bar = super().tabBar()

        # Create a spacer item
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        # Add the spacer item to the tab bar
        tab_bar.setTabButton(tab_bar.count(), QTabBar.LeftSide, spacer)

        return tab_bar
