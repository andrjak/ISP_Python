from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from View import orderPage


class OrderController(QtWidgets.QMainWindow, orderPage.Ui_MainWindow):
    def __init__(self, parent=None, order_list: list = None):
        super(OrderController, self).__init__(parent)
        self.setupUi(self)
        self.order_list = order_list

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Сообщение", "Вы уверены?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
