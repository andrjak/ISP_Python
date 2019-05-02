from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from PyQt5.QtCore import QCoreApplication


from View import mainPage
from View import orderPage
from View import transportPage
from View import workerPage
from PyQt5 import QtWidgets
import sys


class MainController(QtWidgets.QMainWindow, mainPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.options()
        self.pushButton.clicked.connect(self.worker_open)
        self.pushButton_2.clicked.connect(self.order_open)
        self.pushButton_3.clicked.connect(self.transport_open)
        #self.pushButton_4.clicked.connect(self)
        #self.pushButton_5.clicked.connect(self)
        self.pushButton_6.clicked.connect(QCoreApplication.instance().quit)
        self.window = None

    def options(self):
        self.setWindowIcon(QIcon("Image/Bus.png"))
        self.pushButton.setToolTip("Зайдите для управления сотрудниками предприятия")
        self.pushButton_2.setToolTip("Зайдите для управления заказами предприятия")
        self.pushButton_3.setToolTip("Зайдите для управления транспортом предприятия")
        self.pushButton_4.setToolTip("Зайдите для просмотра информации о предприятии")
        self.pushButton_5.setToolTip("Основные настройки приложения")
        # self.showFullScreen()

    def worker_open(self):
        self.window = WorkerController(self)
        self.window.show()
        # self.setVisible(False)

    def order_open(self):
        self.window = OrderController(self)
        self.window.show()
        # self.setVisible(False)

    def transport_open(self):
        self.window = TransportController(self)
        self.window.show()
        # self.setVisible(False)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Сообщение", "Вы уверены?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class WorkerController(QtWidgets.QMainWindow, workerPage.Ui_MainWindow):
    def __init__(self, parent=None):
        super(WorkerController, self).__init__(parent)
        self.setupUi(self)


class TransportController(QtWidgets.QMainWindow, transportPage.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TransportController, self).__init__(parent)
        self.setupUi(self)


class OrderController(QtWidgets.QMainWindow, orderPage.Ui_MainWindow):
    def __init__(self, parent=None):
        super(OrderController, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainController()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
