from PySide6.QtGui import Qt
from models.itemModel import ItemModel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QComboBox, QPushButton, QMessageBox
from controllers.EditMenuController import EditMenuController


def show_error_message(message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setWindowTitle("Error")
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()


class EditMenuWidget(QWidget):
    def __init__(self, itemModel: ItemModel):
        super().__init__()
        self.itemModel = itemModel

        self.TypeDictionary = {
            "Napój": 0,
            "Jedzenie": 1,
            "Deser": 2,
            "Inne": 3
        }

        self.setWindowTitle("Dodać produkt do menu")

        self.MainLayout = QVBoxLayout()
        top_label = QLabel("Dodać produkt do menu")

        FormLayout = QFormLayout()

        type_label = QLabel("Typ produktu")
        self.type_combo = QComboBox()
        self.type_combo.addItem("Napój")
        self.type_combo.addItem("Jedzenie")
        self.type_combo.addItem("Deser")
        self.type_combo.addItem("Inne")
        self.type_combo.setFixedHeight(50)

        # Create labels and line edits
        name_label = QLabel("Nazwa produktu")
        self.name_edit = QLineEdit()
        self.name_edit.setFixedHeight(50)

        price_label = QLabel("Cena sprzedaźy (zł)")
        self.price_edit = QLineEdit()

        cost_label = QLabel("Koszt produkcji (zł)")
        self.cost_edit = QLineEdit()

        url_label = QLabel("URL obrazka z głównego folderu projektu (opcjonalnie)")
        self.url_edit = QLineEdit()

        # Add widgets to the layout
        FormLayout.addWidget(top_label)
        FormLayout.addRow(type_label, self.type_combo)
        FormLayout.addRow(name_label, self.name_edit)
        FormLayout.addRow(price_label, self.price_edit)
        FormLayout.addRow(cost_label, self.cost_edit)
        FormLayout.addRow(url_label, self.url_edit)

        self.addButton = QPushButton("Dodaj produkt do menu")
        self.addButton.setFixedHeight(50)
        self.addButton.clicked.connect(self.add_button_clicked)
        FormLayout.addWidget(self.addButton)

        self.MainLayout.addLayout(FormLayout)

        # TODO implement delete

        self.setLayout(self.MainLayout)

    def add_button_clicked(self):
        try:
            editMenuController = EditMenuController(self.itemModel)
            editMenuController.add_item_menu(self.TypeDictionary[self.type_combo.currentText()], self.name_edit.text(),
                                             int(self.price_edit.text()), int(self.cost_edit.text()),
                                             self.url_edit.text())
        except ValueError as e:
            show_error_message(str(e))
            return
