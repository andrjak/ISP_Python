import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Model import worker
from View import newWorker


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
