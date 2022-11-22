#This file is for saving previous ui designs
#pyQt updates the antenna.py file with its own python code and deletes anything altered about it after running the command-
#pyuic6 -x AntennaAnalyze.ui -o antenna.py


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QFileDialog


class Ui_AntennaRadiationPatternAnalyzer(object):
    def setupUi(self, AntennaRadiationPatternAnalyzer):

        # UI widet setup

        AntennaRadiationPatternAnalyzer.setObjectName("AntennaRadiationPatternAnalyzer")
        AntennaRadiationPatternAnalyzer.resize(1235, 600)
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
        self.manualRunnerContainer_2 = QtWidgets.QFrame(AntennaRadiationPatternAnalyzer)
        self.manualRunnerContainer_2.setGeometry(QtCore.QRect(990, 40, 201, 441))
        self.manualRunnerContainer_2.setStyleSheet("background-color:rgb(211,211,211)")
        self.manualRunnerContainer_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.manualRunnerContainer_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.manualRunnerContainer_2.setObjectName("manualRunnerContainer_2")
        self.headAngleMan_3 = QtWidgets.QLabel(self.manualRunnerContainer_2)
        self.headAngleMan_3.setGeometry(QtCore.QRect(30, 60, 151, 20))
        self.headAngleMan_3.setObjectName("headAngleMan_3")
        self.script_Runner = QtWidgets.QRadioButton(self.manualRunnerContainer_2)
        self.script_Runner.setEnabled(True)
        self.script_Runner.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        self.script_Runner.setFont(font)
        self.script_Runner.setChecked(False)
        self.script_Runner.setAutoExclusive(True)
        self.script_Runner.setObjectName("script_Runner")
        self.angleofarc_4 = QtWidgets.QLabel(self.manualRunnerContainer_2)
        self.angleofarc_4.setGeometry(QtCore.QRect(30, 210, 151, 20))
        self.angleofarc_4.setObjectName("angleofarc_4")
        self.spinBox_3 = QtWidgets.QSpinBox(self.manualRunnerContainer_2)
        self.spinBox_3.setGeometry(QtCore.QRect(30, 250, 141, 22))
        self.spinBox_3.setStyleSheet("background-color:rgb(255,255,255)")
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.manualRunnerContainer_2)
        self.spinBox_4.setGeometry(QtCore.QRect(30, 100, 141, 22))
        self.spinBox_4.setStyleSheet("background-color:rgb(255,255,255)")
        self.spinBox_4.setObjectName("spinBox_4")
        self.homeDevice_2 = QtWidgets.QPushButton(self.manualRunnerContainer_2)
        self.homeDevice_2.setGeometry(QtCore.QRect(30, 390, 141, 41))
        self.homeDevice_2.setStyleSheet("QPushButton {background-color: black; color: white;}")
        self.homeDevice_2.setObjectName("homeDevice_2")
        self.run_script = QtWidgets.QPushButton(self.manualRunnerContainer_2)
        self.run_script.setGeometry(QtCore.QRect(40, 320, 121, 41))
        self.run_script.setObjectName("run_script")

        # function calls
        self.spinBox.setRange(0, 90)
        self.spinBox_2.setRange(-90, 90)
        self.spinBox_3.setRange(0, 90)
        self.spinBox_4.setRange(-90, 90)
        self.manualRunner.toggled.connect(lambda: self.checkManualRadioButton(self.manualRunner))
        self.uploadData.clicked.connect(self.uploadFiles)
        self.spinBox.valueChanged.connect(lambda: self.getSpinValueManual(self.spinBox, 1))
        self.spinBox_2.valueChanged.connect(lambda: self.getSpinValueManual(self.spinBox_2, 2))
        self.run_script.setStyleSheet("border-radius : 50; border: 2px solid black")

        self.retranslateUi(AntennaRadiationPatternAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(AntennaRadiationPatternAnalyzer)

    def retranslateUi(self, AntennaRadiationPatternAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        AntennaRadiationPatternAnalyzer.setWindowTitle(_translate("AntennaRadiationPatternAnalyzer", "Widget"))
        self.uploadData.setText(_translate("AntennaRadiationPatternAnalyzer", "Upload File Data"))
        self.headAngleMan.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Antenna Head?"))
        self.manualRunner.setText(_translate("AntennaRadiationPatternAnalyzer", "Manual Script Runner"))
        self.headAngleMan_2.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Arc Increment?"))
        self.homeDevice.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))
        self.headAngleMan_3.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Antenna Head?"))
        self.script_Runner.setText(_translate("AntennaRadiationPatternAnalyzer", "  Script Runner"))
        self.angleofarc_4.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Arc Increment?"))
        self.homeDevice_2.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))
        self.run_script.setText(_translate("AntennaRadiationPatternAnalyzer", "Run Script"))
        
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
        AntennaRadiationPatternAnalyzer.setWindowTitle(_translate("AntennaRadiationPatternAnalyzer", "AntennaRadiationPatternAnalyzer"))
        self.uploadData.setText(_translate("AntennaRadiationPatternAnalyzer", "Upload File Data"))
        self.headAngleMan.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Antenna Head?"))
        self.manualRunner.setText(_translate("AntennaRadiationPatternAnalyzer", "Manual Script Runner"))
        self.headAngleMan_2.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Arc Increment?"))
        self.homeDevice.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))
        self.headAngleMan_3.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Antenna Head?"))
        self.script_Runner.setText(_translate("AntennaRadiationPatternAnalyzer", "  Script Runner"))
        self.angleofarc_4.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Arc Increment?"))
        self.homeDevice_2.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))
        self.run_script.setText(_translate("AntennaRadiationPatternAnalyzer", "Run Script"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AntennaRadiationPatternAnalyzer = QtWidgets.QWidget()
    ui = Ui_AntennaRadiationPatternAnalyzer()
    ui.setupUi(AntennaRadiationPatternAnalyzer)
    AntennaRadiationPatternAnalyzer.show()
    sys.exit(app.exec())
