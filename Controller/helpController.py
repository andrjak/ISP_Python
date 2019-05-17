from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from View import helpPage

from Model import machineLearning


class HelpController(QtWidgets.QMainWindow, helpPage.Ui_MainWindow):
    def __init__(self, parent=None, file="model.sav"):
        super(HelpController, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_on_help)
        self.model = machineLearning.load(file)

    def click_on_help(self):
        question = self.lineEdit.text()
        qwe = list()
        qwe.append(question)
        predicted = self.model.predict(qwe)
        self.textEdit.setText(predicted[0])

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Сообщение", "Вы уверены?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
