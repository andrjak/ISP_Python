from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Model.transport import Transport, TransportInfo
from View import newTransport


class NewTransportController(QtWidgets.QMainWindow, newTransport.Ui_MainWindow):
    def __init__(self, parent=None, transport_list: list = None):
        super(NewTransportController, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.transport_list = transport_list
        self.pushButton.clicked.connect(self.save_new_transport)

    def save_new_transport(self):
        name = self.lineEdit.text()  # Название модели
        producer = self.lineEdit_2.text()  # Фирма производитель
        year = self.lineEdit_3.text()  # Год выпуска
        warranty_service = self.checkBox.isChecked()  # Гарантийное обслуживание
        insurance = self.checkBox_2.isChecked()  # Есть ли страховка
        try:
            year = int(year)
            warranty_service = bool(warranty_service)
            insurance = bool(insurance)
        except Exception:
            QMessageBox.about(self, "Сообщение!", "Были введены не правильные данные")
        else:
            new_transport = Transport(TransportInfo(name, producer, year), warranty_service, insurance)
            self.transport_list.append(new_transport)
            self.parent.listWidget.addItem(str(new_transport))
            QMessageBox.about(self, "Сообщение!", "Транспорт добавлен")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Сообщение", "Вы уверены?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
