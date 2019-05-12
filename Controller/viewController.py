import datetime

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets

from View import mainPage, helpPage
from View import orderPage
from View import transportPage
from View import workerPage
from View import newWorker

from Controller.helpController import HelpController
from Controller.workerController import WorkerController

import company
import worker
import order
import transport
import sys


class MainController(QtWidgets.QMainWindow, mainPage.Ui_MainWindow):
    def __init__(self, worker_list, order_list, transport_list, position_dict):
        super().__init__()
        self.worker_list = worker_list
        self.order_list = order_list
        self.transport_list = transport_list
        self.position_dict = position_dict
        self.setupUi(self)
        self.options()
        self.window = None

    def options(self):
        self.setWindowIcon(QIcon("Image/Bus.png"))
        self.pushButton.setToolTip("Зайдите для управления сотрудниками предприятия")
        self.pushButton_2.setToolTip("Зайдите для управления заказами предприятия")
        self.pushButton_3.setToolTip("Зайдите для управления транспортом предприятия")
        self.pushButton_4.setToolTip("Зайдите для просмотра информации о предприятии")
        self.pushButton_5.setToolTip("Основные настройки приложения")
        self.pushButton.clicked.connect(self.worker_open)
        self.pushButton_2.clicked.connect(self.order_open)
        self.pushButton_3.clicked.connect(self.transport_open)
        # self.pushButton_4.clicked.connect(self)
        # self.pushButton_5.clicked.connect(self)
        self.pushButton_6.clicked.connect(QCoreApplication.instance().quit)
        # self.showFullScreen()

    def worker_open(self):
        self.window = WorkerController(self, self.worker_list, self.position_dict)
        self.window.show()
        # self.setVisible(False)

    def order_open(self):
        self.window = OrderController(self, self.order_list)
        self.window.show()
        # self.setVisible(False)

    def transport_open(self):
        self.window = TransportController(self, self.transport_list)
        self.window.show()
        # self.setVisible(False)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Сообщение", "Вы уверены?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


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


def main(main_company: company.Company):

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainController(main_company.workerList, main_company.orderList, main_company.transportList,
                            main_company.positionDict)  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())


if __name__ == "__main__":
    pass
