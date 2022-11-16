#This file is for saving previous ui designs
#pyQt updates the antenna.py file with its own python code and deletes anything altered about it after running the command-
#pyuic6 -x AntennaAnalyze.ui -o antenna.py


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QFileDialog


class Ui_AntennaRadiationPatternAnalyzer(object):
    def setupUi(self, AntennaRadiationPatternAnalyzer):

        #UI widet setup
        AntennaRadiationPatternAnalyzer.setObjectName("AntennaRadiationPatternAnalyzer")
        AntennaRadiationPatternAnalyzer.resize(1223, 600)
        AntennaRadiationPatternAnalyzer.setStyleSheet("")
        self.uploadData = QtWidgets.QPushButton(AntennaRadiationPatternAnalyzer)
        self.uploadData.setGeometry(QtCore.QRect(330, 510, 121, 41))
        self.uploadData.setObjectName("uploadData")
        self.manualRunnerContainer = QtWidgets.QFrame(AntennaRadiationPatternAnalyzer)
        self.manualRunnerContainer.setGeometry(QtCore.QRect(30, 40, 201, 441))
        self.manualRunnerContainer.setStyleSheet("background-color:rgb(211,211,211)")
        self.manualRunnerContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.manualRunnerContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.manualRunnerContainer.setObjectName("manualRunnerContainer")
        self.headAngleMan = QtWidgets.QLabel(self.manualRunnerContainer)
        self.headAngleMan.setGeometry(QtCore.QRect(30, 60, 151, 20))
        self.headAngleMan.setObjectName("headAngleMan")
        self.manualRunner = QtWidgets.QRadioButton(self.manualRunnerContainer)
        self.manualRunner.setEnabled(True)
        self.manualRunner.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        self.manualRunner.setFont(font)
        self.manualRunner.setChecked(False)
        self.manualRunner.setAutoExclusive(True)
        self.manualRunner.setObjectName("manualRunner")
        self.headAngleMan_2 = QtWidgets.QLabel(self.manualRunnerContainer)
        self.headAngleMan_2.setGeometry(QtCore.QRect(30, 210, 151, 20))
        self.headAngleMan_2.setObjectName("headAngleMan_2")
        self.spinBox = QtWidgets.QSpinBox(self.manualRunnerContainer)
        self.spinBox.setGeometry(QtCore.QRect(30, 250, 141, 22))
        self.spinBox.setStyleSheet("background-color:rgb(255,255,255)")
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.manualRunnerContainer)
        self.spinBox_2.setGeometry(QtCore.QRect(30, 100, 141, 22))
        self.spinBox_2.setStyleSheet("background-color:rgb(255,255,255)")
        self.spinBox_2.setObjectName("spinBox_2")
        self.homeDevice = QtWidgets.QPushButton(self.manualRunnerContainer)
        self.homeDevice.setGeometry(QtCore.QRect(30, 350, 141, 41))
        self.homeDevice.setStyleSheet("QPushButton {background-color: black; color: white;}")
        self.homeDevice.setObjectName("homeDevice")
        self.spinBox.setRange(0,90)
        self.spinBox_2.setRange(-90,90)

        #function calls
        self.manualRunner.toggled.connect(lambda: self.checkManualRadioButton(self.manualRunner))
        self.uploadData.clicked.connect(self.uploadFiles)
        self.spinBox.valueChanged.connect(lambda : self.getSpinValueManual(self.spinBox,1))
        self.spinBox_2.valueChanged.connect(lambda :self.getSpinValueManual(self.spinBox_2,2))

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
    def getSpinValueManual(self, spinbox, val):
        if(val == 2):
            value = spinbox.value()
            print("spinbox1:",value)
        if(val == 1):
            value2 = spinbox.value()
            print("spinbox2:",value2)
    def retranslateUi(self, AntennaRadiationPatternAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        AntennaRadiationPatternAnalyzer.setWindowTitle(_translate("AntennaRadiationPatternAnalyzer", "Antenna Radiation Pattern Analyzer"))
        self.uploadData.setText(_translate("AntennaRadiationPatternAnalyzer", "Upload File Data"))
        self.headAngleMan.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Antenna Head?"))
        self.manualRunner.setText(_translate("AntennaRadiationPatternAnalyzer", "Manual Script Runner"))
        self.headAngleMan_2.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Arc Increment?"))
        self.homeDevice.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AntennaRadiationPatternAnalyzer = QtWidgets.QWidget()
    ui = Ui_AntennaRadiationPatternAnalyzer()
    ui.setupUi(AntennaRadiationPatternAnalyzer)
    AntennaRadiationPatternAnalyzer.show()
    sys.exit(app.exec())
