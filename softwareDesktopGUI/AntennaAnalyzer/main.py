#This file is for saving previous ui designs
#pyQt updates the antenna.py file with its own python code and deletes anything altered about it after running the command-
#pyuic6 -x AntennaAnalyze.ui -o antenna.py


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1067, 600)
        Widget.setStyleSheet("")
        self.manualRunner = QtWidgets.QRadioButton(Widget)
        self.manualRunner.setEnabled(True)
        self.manualRunner.setGeometry(QtCore.QRect(30, 50, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.manualRunner.setFont(font)
        self.manualRunner.setChecked(False)
        self.manualRunner.setAutoExclusive(True)
        self.manualRunner.setObjectName("manualRunner")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(50, 360, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet( " background-color: black; color: white")
        self.manualRunner.toggled.connect(lambda: self.checkManualRadioButton(self.manualRunner))

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
    def checkManualRadioButton(self, b):
        if(b.isChecked()):
            print("here")
        else:
            print("h")
    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Antenna Radiation Analyzer"))
        self.manualRunner.setText(_translate("Widget", "Manual Script Runner"))
        self.pushButton.setText(_translate("Widget", "Home Device"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())
