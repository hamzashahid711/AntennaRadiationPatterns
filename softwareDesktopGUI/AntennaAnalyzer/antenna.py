# Form implementation generated from reading ui file 'AntennaAnalyze.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


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
        font.setItalic(False)
        self.manualRunner.setFont(font)
        self.manualRunner.setChecked(False)
        self.manualRunner.setAutoExclusive(True)
        self.manualRunner.setObjectName("manualRunner")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(50, 360, 121, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

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
