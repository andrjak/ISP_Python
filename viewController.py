from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from PyQt5.QtCore import QCoreApplication


from View import mainPage
from View import orderPage
from View import transportPage
from View import workerPage
from PyQt5 import QtWidgets
import worker
import order
import transport
import sys


class MainController(QtWidgets.QMainWindow, mainPage.Ui_MainWindow):
    def __init__(self, worker_list, order_list, transport_list):
        super().__init__()
        self.worker_list = worker_list
        self.order_list = order_list
        self.transport_list = transport_list
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
        #self.pushButton_4.clicked.connect(self)
        #self.pushButton_5.clicked.connect(self)
        self.pushButton_6.clicked.connect(QCoreApplication.instance().quit)
        # self.showFullScreen()

    def worker_open(self):
        self.window = WorkerController(self, self.worker_list)
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


class WorkerController(QtWidgets.QMainWindow, workerPage.Ui_MainWindow):
    def __init__(self, parent=None, worker_list: list = None):
        super(WorkerController, self).__init__(parent)
        self.setupUi(self)
        self.worker_list = worker_list
        self.options()
        # worker_list = range(100)
        for i in worker_list:
            self.listWidget.addItem(str(i))

    def options(self):
        self.pushButton_2.clicked.connect(self.del_worker)
        # self.showFullScreen()

    def add_worker(self):
        pass

    def del_worker(self):
        list_items = self.listWidget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            index = self.listWidget.row(item)
            self.listWidget.takeItem(index)
            self.worker_list.remove(self.worker_list[index])

    def sort(self):
        self.listWidget.clear()
        self.worker_list.sort(key=lambda this_worker: this_worker.name)
        for i in self.worker_list:
            self.listWidget.addItem(str(i))


class TransportController(QtWidgets.QMainWindow, transportPage.Ui_MainWindow):
    def __init__(self, parent=None, transport_list: list = None):
        super(TransportController, self).__init__(parent)
        self.setupUi(self)
        self.transport_list = transport_list


class OrderController(QtWidgets.QMainWindow, orderPage.Ui_MainWindow):
    def __init__(self, parent=None, order_list: list = None):
        super(OrderController, self).__init__(parent)
        self.setupUi(self)
        self.transport_list = order_list


def main(worker_list, order_list, transport_list):
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainController(worker_list, order_list, transport_list)  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(None, None, None)
