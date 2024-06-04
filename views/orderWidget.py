from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QPushButton


# 0 - beverage 1 - food 2 - dessert 3 - other
class OrderWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zlożyć zamówienie")
        self.tab_widget = QTabWidget()

        def create_tabs(self):
            layout = QVBoxLayout()

            # Створення вкладок, подібних до тих, що на зображенні
            tabs = [
                ("Штори", self.create_tab_content, self.save_button_clicked),
                ("Тюль", self.create_tab_content, self.save_button_clicked),
                ("Мереживо", self.create_tab_content, self.save_button_clicked),
                ("Фурнітура", self.create_tab_content, self.save_button_clicked),
            ]

            for tab_name, content_creator, save_func in tabs:
                tab = QWidget()
                tab_layout = QVBoxLayout()
                tab_content = content_creator()
                tab_layout.addLayout(tab_content)

                save_button = QPushButton("Зберегти")
                save_button.clicked.connect(save_func)
                tab_layout.addWidget(save_button, alignment=Qt.AlignRight)

                tab.setLayout(tab_layout)
                self.tab_widget.addTab(tab, tab_name)

            layout.addWidget(self.tab_widget)
            self.setLayout(layout)

