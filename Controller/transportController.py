from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Controller.helpController import HelpController
from Controller.newTransportController import NewTransportController
from View import transportPage


class TransportController(QtWidgets.QMainWindow, transportPage.Ui_MainWindow):
    def __init__(self, parent=None, transport_list: list = None):
        super(TransportController, self).__init__(parent)
        self.setupUi(self)
        self.transport_list = transport_list
        self.window = None
        self.options()

    def options(self):
        self.pushButton.clicked.connect(self.add_transport)
        self.pushButton_2.clicked.connect(self.del_transport)
        self.pushButton_3.clicked.connect(self.sort)
        self.pushButton_4.clicked.connect(self.get_producer_info)
        self.pushButton_5.clicked.connect(self.get_model_info)
        self.pushButton_6.clicked.connect(self.close)
        self.Help.clicked.connect(self.open_help)
        for i in self.transport_list:
            self.listWidget.addItem(str(i))

    def open_help(self):
        self.window = HelpController(self, "model2.sav")
        self.window.show()

    def add_transport(self):
        self.window = NewTransportController(self, self.transport_list)
        self.window.show()

    def del_transport(self):
        list_items = self.listWidget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            index = self.listWidget.row(item)
            self.listWidget.takeItem(index)
            self.transport_list.remove(self.transport_list[index])

    def sort(self):
        self.listWidget.clear()
        if self.comboBox.currentText() == "По фирме и модели":
            self.transport_list.sort(key=lambda this_transport: this_transport.info.producer)
        elif self.comboBox.currentText() == "По году выпуска":
            self.transport_list.sort(key=lambda this_transport: this_transport.info.year)
        for i in self.transport_list:
            self.listWidget.addItem(str(i))

    def get_producer_info(self):
        list_items = self.listWidget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            index = self.listWidget.row(item)
            self.transport_list[index].info.get_producer_info()

    def get_model_info(self):
        list_items = self.listWidget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            index = self.listWidget.row(item)
            self.transport_list[index].info.get_model_info()

    def close(self):
        self.destroy()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Сообщение", "Вы уверены?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
