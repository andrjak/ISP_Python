from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets


from View import mainPage

from Controller.workerController import WorkerController
from Controller.orderController import OrderController
from Controller.transportController import TransportController

from Model import company, DBcontroler
import sys


class MainController(QtWidgets.QMainWindow, mainPage.Ui_MainWindow):
    def __init__(self, main_company):
        super().__init__()
        self.worker_list = main_company.workerList
        self.order_list = main_company.orderList
        self.transport_list = main_company.transportList
        self.position_dict = main_company.positionDict
        self.main_company = main_company
        self.setupUi(self)
        self.options()
        self.window = None

    def options(self):
        self.setWindowIcon(QIcon("Image/Bus.png"))
        self.pushButton.setToolTip("Зайдите для управления сотрудниками предприятия")
        self.pushButton_2.setToolTip("Зайдите для управления заказами предприятия")
        self.pushButton_3.setToolTip("Зайдите для управления транспортом предприятия")
        self.pushButton_4.setToolTip("Нажмите чтобы сохранить все внесённые изменения")
        self.pushButton.clicked.connect(self.worker_open)
        self.pushButton_2.clicked.connect(self.order_open)
        self.pushButton_3.clicked.connect(self.transport_open)
        self.pushButton_4.clicked.connect(self.save_data)
        self.pushButton_6.clicked.connect(QCoreApplication.instance().quit)
        # self.showFullScreen()

    def save_data(self):
        DBcontroler.set_data(self.main_company)

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


def main(main_company: company.Company):

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainController(main_company)  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())


if __name__ == "__main__":
    pass
