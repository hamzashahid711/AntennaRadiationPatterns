#This file is for saving previous ui designs
#pyQt updates the antenna.py file with its own python code and deletes anything altered about it after running the command-
#pyuic6 -x AntennaAnalyze.ui -o antenna.py


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QFileDialog


class Ui_AntennaRadiationPatternAnalyzer(object):
    def setupUi(self, AntennaRadiationPatternAnalyzer):
        AntennaRadiationPatternAnalyzer.setObjectName("AntennaRadiationPatternAnalyzer")
        AntennaRadiationPatternAnalyzer.resize(1223, 600)
        AntennaRadiationPatternAnalyzer.setStyleSheet("")
        self.manualRunner = QtWidgets.QRadioButton(AntennaRadiationPatternAnalyzer)
        self.manualRunner.setEnabled(True)
        self.manualRunner.setGeometry(QtCore.QRect(30, 50, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        self.manualRunner.setFont(font)
        self.manualRunner.setChecked(False)
        self.manualRunner.setAutoExclusive(True)
        self.manualRunner.setObjectName("manualRunner")
        self.manualRunner.toggled.connect(lambda: self.checkManualRadioButton(self.manualRunner))
        self.homeDevice = QtWidgets.QPushButton(AntennaRadiationPatternAnalyzer)
        self.homeDevice.setGeometry(QtCore.QRect(50, 360, 121, 31))
        self.homeDevice.setStyleSheet(" background-color: Black; color: white }")
        self.homeDevice.setObjectName("homeDevice")
        self.uploadData = QtWidgets.QPushButton(AntennaRadiationPatternAnalyzer)
        self.uploadData.setGeometry(QtCore.QRect(330, 520, 111, 31))
        self.uploadData.setObjectName("uploadData")
        self.uploadData.clicked.connect(self.uploadFiles)

        self.retranslateUi(AntennaRadiationPatternAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(AntennaRadiationPatternAnalyzer)

    def checkManualRadioButton(self, b):
        if (b.isChecked()):
            print("here")
        else:
            print("h")

    def uploadFiles(self):
        fileName = QFileDialog.getOpenFileName(None, 'Open File', "", "Image Files (*.png)")
        print(fileName)
        if (fileName[0] != '' and fileName[1] != ''):
            print("uploaded success")
            self.successPopup(fileName[0])
        else:
            print("failed to upload file try again")

    def successPopup(self, path):
        msg = QMessageBox()
        msg.setWindowTitle("Pop Up")
        msg.setText("Upload Successful from " + path)

        x = msg.exec()
    def retranslateUi(self, AntennaRadiationPatternAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        AntennaRadiationPatternAnalyzer.setWindowTitle(_translate("AntennaRadiationPatternAnalyzer", "Widget"))
        self.manualRunner.setText(_translate("AntennaRadiationPatternAnalyzer", "Manual Script Runner"))
        self.homeDevice.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))
        self.uploadData.setText(_translate("AntennaRadiationPatternAnalyzer", "Upload File Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AntennaRadiationPatternAnalyzer = QtWidgets.QWidget()
    ui = Ui_AntennaRadiationPatternAnalyzer()
    ui.setupUi(AntennaRadiationPatternAnalyzer)
    AntennaRadiationPatternAnalyzer.show()
    sys.exit(app.exec())
