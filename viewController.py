import datetime

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets

from View import mainPage
from View import orderPage
from View import transportPage
from View import workerPage
from View import newWorker

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


class WorkerController(QtWidgets.QMainWindow, workerPage.Ui_MainWindow):
    def __init__(self, parent=None, worker_list: list = None, position_dict: dict = None):
        super(WorkerController, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.worker_list = worker_list
        self.position_dict = position_dict
        self.options()
        self.window = None
        self.flag = True

    def options(self):
        self.pushButton.clicked.connect(self.add_worker)
        self.pushButton_2.clicked.connect(self.del_worker)
        # self.pushButton_3
        # self.pushButton_4.clicked.connect(self.view_position)
        # self.pushButton_5
        # self.pushButton_6.clicked.connect(self.del_position)
        self.pushButton_7.clicked.connect(self.view_worker)
        self.pushButton_8.clicked.connect(self.search)
        self.pushButton_9.clicked.connect(self.sort)
        self.pushButton_10.clicked.connect(self.birthday_sort)
        for i in self.worker_list:
            self.listWidget.addItem(str(i))

    def add_worker(self):
        if self.flag:
            self.window = NewWorkerController(self, self.worker_list)
            self.window.show()

    def del_worker(self):
        if self.flag:
            list_items = self.listWidget.selectedItems()
            if not list_items:
                return
            for item in list_items:
                index = self.listWidget.row(item)
                self.listWidget.takeItem(index)
                self.worker_list.remove(self.worker_list[index])

    def view_worker(self):
            self.flag = True
            self.listWidget.clear()
            for i in self.worker_list:
                self.listWidget.addItem(str(i))

    def change_position(self):
        if not self.flag:
            pass

    def view_position(self):
        self.flag = False
        self.listWidget.clear()
        for key, value in self.position_dict:
            self.listWidget.addItem("{}: {}".format(str(key), str(value)))

    def add_position(self):
        if not self.flag:
            pass

    def del_position(self):
        if not self.flag:
            dict_items = self.listWidget.selectedItems()
            del_array = []
            if not dict_items:
                return
            for item in dict_items:
                index = self.listWidget.row(item)
                self.listWidget.takeItem(index)
                dict_items.append(index)
            counter = 0
            for key, value in self.position_dict:
                if counter in del_array:
                    del del_array[key]
                counter += 1

    def search(self):
        item = None
        item = self.lineEdit.text()
        if item is not None:
            self.listWidget.clear()
            for i in self.worker_list:
                if item in i.name:
                    self.listWidget.addItem(str(i))

    def sort(self):
        if self.flag:
            self.listWidget.clear()
            if self.comboBox.currentText() == "Сортировать по имени":
                self.worker_list.sort(key=lambda this_worker: this_worker.name)
            elif self.comboBox.currentText() == "Сортировать по дате рождения":
                self.worker_list.sort(key=lambda this_worker: this_worker.birthday)
            else:
                self.worker_list.sort(key=lambda this_worker: this_worker.salary)
            for i in self.worker_list:
                self.listWidget.addItem(str(i))

    def birthday_sort(self):
        self.listWidget.clear()
        for i in self.worker_list:
            if i.birthday.month == datetime.date.today().month:
                self.listWidget.addItem(str(i))

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


class NewWorkerController(QtWidgets.QMainWindow, newWorker.Ui_MainWindow):
    def __init__(self, parent=None, worker_list: list = None):
        super(NewWorkerController, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.worker_list = worker_list
        self.pushButton.clicked.connect(self.save_new_worker)

    def save_new_worker(self):
        name = self.lineEdit.text()
        position = self.lineEdit_2.text()
        date = self.lineEdit_3.text()
        duration = self.lineEdit_4.text()
        salary = self.lineEdit_5.text()
        experience = self.lineEdit_6.text()
        birthday = self.lineEdit_7.text()

        try:
            birthday = datetime.datetime.strptime(birthday, "%d.%m.%Y")
            salary = int(salary)
            experience = int(experience)
            duration = int(duration)
            date = datetime.datetime.strptime(date, "%d.%m.%Y")
        except Exception:
            QMessageBox.about(self, "Сообщение!", "Были введены не правильные данные")
        else:
            new_worker = worker.Worker(name, position, birthday, salary, experience, duration, date)
            self.worker_list.append(new_worker)
            self.parent.listWidget.addItem(str(new_worker))
            QMessageBox.about(self, "Сообщение!", "Работник добавлен")

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
