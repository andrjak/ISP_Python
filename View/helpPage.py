# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpPage.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 334)
        MainWindow.setStyleSheet("QMainWindow { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0)); font: 10pt \"MS Shell Dlg 2\"; } \n"
"QLabel {color: rgb(85, 41, 9); }\n"
"QPushButton { background-color: rgb(255, 228, 144); color: rgb(85, 41, 9); font: 10pt \"MS Shell Dlg 2\"; }\n"
"QComboBox { background-color: rgb(255, 228, 144); color: rgb(85, 41, 9); font: 10pt \"MS Shell Dlg 2\";}\n"
"QLineEdit { background-color: rgb(255, 245, 187); color: rgb(85, 41, 9); font: 10pt \"MS Shell Dlg 2\";}\n"
"QListWidget { background-color: rgb(255, 245, 187); color: rgb(85, 41, 9); font: 10pt \"MS Shell Dlg 2\";}\n"
"QTextEdit { background-color: rgb(255, 245, 187); color: rgb(85, 41, 9); font: 10pt \"MS Shell Dlg 2\";}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Справка"))
        self.pushButton.setText(_translate("MainWindow", "Задать вопрос"))
        self.label.setText(_translate("MainWindow", "Ответ на запрос"))


