import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Controller.newWorkerController import NewWorkerController
from Controller.helpController import HelpController
from View import workerPage


class WorkerController(QtWidgets.QMainWindow, workerPage.Ui_MainWindow):
    def __init__(self, parent=None, worker_list: list = None, position_dict: dict = None):
        super(WorkerController, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.worker_list = worker_list
        self.position_dict = position_dict
        self.options()
        self.window = None

    def options(self):
        self.pushButton.clicked.connect(self.add_worker)
        self.pushButton_2.clicked.connect(self.del_worker)
        self.pushButton_7.clicked.connect(self.view_worker)
        self.pushButton_8.clicked.connect(self.search)
        self.pushButton_9.clicked.connect(self.sort)
        self.pushButton_10.clicked.connect(self.birthday_sort)
        self.back.clicked.connect(self.close)
        self.Help.clicked.connect(self.open_help)
        for i in self.worker_list:
            self.listWidget.addItem(str(i))

    def open_help(self):
        self.window = HelpController(self)
        self.window.show()

    def add_worker(self):
        self.window = NewWorkerController(self, self.worker_list)
        self.window.show()

    def del_worker(self):
        list_items = self.listWidget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            index = self.listWidget.row(item)
            self.listWidget.takeItem(index)
            self.worker_list.remove(self.worker_list[index])

    def view_worker(self):
            self.listWidget.clear()
            for i in self.worker_list:
                self.listWidget.addItem(str(i))

    def change_position(self):
        pass

    def view_position(self):
        self.listWidget.clear()
        for key, value in self.position_dict:
            self.listWidget.addItem("{}: {}".format(str(key), str(value)))

    def add_position(self):
        pass

    def del_position(self):
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
        item = self.lineEdit.text()
        if item is not None:
            self.listWidget.clear()
            for i in self.worker_list:
                if item in i.name:
                    self.listWidget.addItem(str(i))

    def sort(self):
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

    def close(self):
        self.destroy()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Сообщение", "Вы уверены?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
