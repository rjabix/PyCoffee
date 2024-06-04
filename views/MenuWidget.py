from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, \
    QLineEdit, QSizePolicy, QGridLayout
from views.MenuItemButton import MenuItemButton


class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")

        with open("assets/menuwindow_style.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.tab_widget = QTabWidget()

        self.beverages_tab = self.create_tab("Drinks", [("menu item 0", "2$", "path_to_image0.jpg"), ("menu item 1", "3$", "path_to_image1.jpg"), ("menu item 2", "4$", "path_to_image2.jpg"), ("menu item 3", "5$", "path_to_image3.jpg"), ("menu item 4", "6$", "path_to_image4.jpg")])
        self.food_tab = self.create_tab("Food", [("menu item 5", "7$", "path_to_image5.jpg"), ("menu item 6", "8$", "path_to_image6.jpg"), ("menu item 7", "9$", "path_to_image7.jpg"), ("menu item 8", "10$", "path_to_image8.jpg")])
        self.dessert_tab = self.create_tab("Desserts", [("menu item 9", "11$", "path_to_image9.jpg"), ("menu item 10", "12$", "path_to_image10.jpg"), ("menu item 11", "13$", "path_to_image11.jpg")])
        self.other_tab = self.create_tab("Other", [("menu item 12", "14$", "path_to_image12.jpg"), ("menu item 13", "15$", "path_to_image13.jpg"), ("menu item 14", "16$", "path_to_image14.jpg"), ("menu item 15", "17$", "path_to_image15.jpg"), ("menu item 16", "18$", "path_to_image16.jpg")])

        # Add tabs to the tab widget
        self.tab_widget.addTab(self.beverages_tab, "Napoje")
        self.tab_widget.addTab(self.food_tab, "Jedzenie")
        self.tab_widget.addTab(self.dessert_tab, "Deserty")
        self.tab_widget.addTab(self.other_tab, "Inne")

        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def create_tab(self, tab_name, items):
        # Create a scrollable area for the tab content
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a grid layout for the tab content
        grid_layout = QGridLayout()
        content_widget = QWidget()
        content_widget.setLayout(grid_layout)

        # Add menu items as buttons to the grid layout
        items_per_row = 3

        for index, (item, price, image_path) in enumerate(items):
            menu_item_button = MenuItemButton(item, price, image_path)
            menu_item_button.setObjectName("menu_item_button")

            # Calculate the row and column index
            row = index // items_per_row
            col = index % items_per_row

            grid_layout.addWidget(menu_item_button, row, col)

        scroll_area.setWidget(content_widget)

        # Return the scrollable area as the tab widget
        return scroll_area

