from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from View import transportPage


class TransportController(QtWidgets.QMainWindow, transportPage.Ui_MainWindow):
    def __init__(self, parent=None, transport_list: list = None):
        super(TransportController, self).__init__(parent)
        self.setupUi(self)
        self.transport_list = transport_list

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Сообщение", "Вы уверены?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
