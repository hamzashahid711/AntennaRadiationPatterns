#This file is for saving previous ui designs
#pyQt updates the antenna.py file with its own python code and deletes anything altered about it after running the command-
#pyuic6 -x AntennaAnalyze.ui -o antenna.py
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from matplotlib import pyplot as plt
import random
import os
from PIL import Image
from tempfile import NamedTemporaryFile

class Ui_AntennaRadiationPatternAnalyzer(object):
    def setupUi(self, AntennaRadiationPatternAnalyzer):

        # UI widet setup
        AntennaRadiationPatternAnalyzer.setObjectName("AntennaRadiationPatternAnalyzer")
        AntennaRadiationPatternAnalyzer.resize(1235, 600)
        AntennaRadiationPatternAnalyzer.setStyleSheet("")
        self.manualRunnerContainer = QtWidgets.QFrame(AntennaRadiationPatternAnalyzer)
        self.manualRunnerContainer.setGeometry(QtCore.QRect(30, 50, 201, 431))
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
        self.manualRunnerContainer_2.setGeometry(QtCore.QRect(990, 50, 221, 431))
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
        self.homeDevice_2.setGeometry(QtCore.QRect(30, 380, 141, 41))
        self.homeDevice_2.setStyleSheet("QPushButton {background-color: black; color: white;}")
        self.homeDevice_2.setObjectName("homeDevice_2")
        self.run_script = QtWidgets.QPushButton(self.manualRunnerContainer_2)
        self.run_script.setGeometry(QtCore.QRect(40, 320, 121, 41))
        self.run_script.setStyleSheet("background-color:rgb(255,255,255)")
        self.run_script.setObjectName("run_script")
        self.buttonContainer = QtWidgets.QFrame(AntennaRadiationPatternAnalyzer)
        self.buttonContainer.setGeometry(QtCore.QRect(270, 530, 691, 61))
        self.buttonContainer.setStyleSheet("background-color:rgb(211,211,211)")
        self.buttonContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.buttonContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.buttonContainer.setObjectName("buttonContainer")
        self.uploadData = QtWidgets.QPushButton(self.buttonContainer)
        self.uploadData.setGeometry(QtCore.QRect(40, 10, 121, 41))
        self.uploadData.setStyleSheet("background-color:rgb(255,255,255)\n"
                                      "")
        self.uploadData.setObjectName("uploadData")
        self.exportData = QtWidgets.QPushButton(self.buttonContainer)
        self.exportData.setGeometry(QtCore.QRect(280, 10, 121, 41))
        self.exportData.setStyleSheet("background-color:rgb(255,255,255)")
        self.exportData.setObjectName("Export Data")
        self.changeView = QtWidgets.QPushButton(self.buttonContainer)
        self.changeView.setGeometry(QtCore.QRect(530, 10, 121, 41))
        self.changeView.setStyleSheet("background-color:rgb(255,255,255)\n"
                                      "")
        self.changeView.setObjectName("changeView")
        self.fruqencyMapContainer = QtWidgets.QFrame(AntennaRadiationPatternAnalyzer)
        self.fruqencyMapContainer.setGeometry(QtCore.QRect(260, 0, 701, 61))
        self.fruqencyMapContainer.setStyleSheet("background-color:rgb(211,211,211)")
        self.fruqencyMapContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fruqencyMapContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fruqencyMapContainer.setObjectName("fruqencyMapContainer")
        self.mapFrequency = QtWidgets.QPushButton(self.fruqencyMapContainer)
        self.mapFrequency.setGeometry(QtCore.QRect(530, 10, 121, 41))
        self.mapFrequency.setStyleSheet("background-color:rgb(255,255,255)")
        self.mapFrequency.setObjectName("mapFrequency")
        self.frequencyInputLabel = QtWidgets.QLabel(self.fruqencyMapContainer)
        self.frequencyInputLabel.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.frequencyInputLabel.setObjectName("frequencyInputLabel")
        self.hz = QtWidgets.QLabel(self.fruqencyMapContainer)
        self.hz.setGeometry(QtCore.QRect(220, 20, 58, 16))
        self.hz.setObjectName("hz")
        self.spinBox_5 = QtWidgets.QSpinBox(self.fruqencyMapContainer)
        self.spinBox_5.setGeometry(QtCore.QRect(130, 11, 81, 31))
        self.spinBox_5.setStyleSheet("background-color:rgb(255,255,255)")
        self.spinBox_5.setObjectName("spinBox_5")
        self.imagePlot = QtWidgets.QLabel(AntennaRadiationPatternAnalyzer)
        self.imagePlot.setGeometry(QtCore.QRect(300, 70, 681, 441))
        self.imagePlot.setText("")
        self.imagePlot.setObjectName("imagePlot")

        #initial state
        self.manualRunner.setChecked(True)
        self.disableScript(self.manualRunner, self.script_Runner,self.spinBox, self.spinBox_2, self.spinBox_3,self.spinBox_4,self.homeDevice, self.homeDevice_2)
        # function calls
        self.mapFrequency.clicked.connect(self.plot)
        self.homeDevice.clicked.connect(self.homedevice)
        self.homeDevice_2.clicked.connect(self.homedevice)
        self.spinBox.setRange(0, 90)
        self.spinBox_2.setRange(-90, 90)
        self.spinBox_3.setRange(0, 90)
        self.spinBox_4.setRange(-90, 90)
        self.manualRunner.toggled.connect(lambda: self.disableManual(self.manualRunner,self.script_Runner,self.spinBox,self.spinBox_2,self.spinBox_3,self.spinBox_4,self.homeDevice,self.homeDevice_2))
        self.script_Runner.toggled.connect(lambda: self.disableScript(self.manualRunner,self.script_Runner,self.spinBox,self.spinBox_2,self.spinBox_3,self.spinBox_4,self.homeDevice,self.homeDevice_2))

        self.uploadData.clicked.connect(self.uploadFiles)
        self.spinBox.valueChanged.connect(lambda: self.getSpinValueManual(self.spinBox, 1))
        self.spinBox_2.valueChanged.connect(lambda: self.getSpinValueManual(self.spinBox_2, 2))
        self.run_script.setStyleSheet("border-radius : 50; border: 2px solid black")

        self.retranslateUi(AntennaRadiationPatternAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(AntennaRadiationPatternAnalyzer)

    def homedevice(self):
        msg = QMessageBox()
        msg.setWindowTitle("Pop Up")
        msg.setText("homing device")

        x = msg.exec()

    def plot(self):
        r = np.arange(0, 2, 0.01)
        theta = 2 * np.pi * r

        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.plot(theta, r)
        ax.set_rmax(2)
        ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
        ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
        ax.grid(True)

        ax.set_title("A line plot on a polar axis", va='bottom')

        with NamedTemporaryFile("r+b", delete=True) as plot:
            fig1 = plt.gcf()
            plt.show()
            plt.draw()
            # delete is by default True
            # the if you don't set it, it will delete the file
            # after leaving the with block
            fig1.savefig(plot)
            # seeking back to position 0
            # allowed by r+
            plot.seek(0)
            # show the image from temporary file with PILLOW
            qpix = QPixmap(plot.name)
            self.imagePlot.setPixmap(qpix)
            # Image is shown (window opens)
            # but then directly the block is left and the NamedTemporaryFile is deleted
        if os.path.exists(plot.name):
            print("still exists.")
        else:
            print(plot.name + "was deleted.")


    def disableManual(self, radioButton1, radioButton2, spinbox1, spinbox2, spinbox3, spinbox4, homeDeviceButton, homeDeviceButton2):
        print("script runner mode initiated")
        radioButton1.setEnabled(False)
        spinbox1.setEnabled(False)
        spinbox2.setEnabled(False)
        radioButton2.setEnabled(True)
        homeDeviceButton.setEnabled(False)
        spinbox3.setEnabled(True)
        spinbox4.setEnabled(True)
        homeDeviceButton2.setEnabled(True)

    def disableScript(self, radioButton1, radioButton2, spinbox1, spinbox2, spinbox3 , spinbox4,homeDeviceButton, homeDeviceButton2):
        print("manual runner mode initiated")
        radioButton2.setEnabled(False)
        spinbox3.setEnabled(False)
        spinbox4.setEnabled(False)
        radioButton1.setEnabled(True)
        homeDeviceButton2.setEnabled(False)
        spinbox1.setEnabled(True)
        spinbox2.setEnabled(True)
        homeDeviceButton.setEnabled(True)


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
        AntennaRadiationPatternAnalyzer.setWindowTitle(_translate("AntennaRadiationPatternAnalyzer", "Widget"))
        self.headAngleMan.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Antenna Head?"))
        self.manualRunner.setText(_translate("AntennaRadiationPatternAnalyzer", "Manual Script Runner"))
        self.headAngleMan_2.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Arc Increment?"))
        self.homeDevice.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))
        self.headAngleMan_3.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Antenna Head?"))
        self.script_Runner.setText(_translate("AntennaRadiationPatternAnalyzer", "  Script Runner"))
        self.angleofarc_4.setText(_translate("AntennaRadiationPatternAnalyzer", "Angle of Arc Increment?"))
        self.homeDevice_2.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))
        self.run_script.setText(_translate("AntennaRadiationPatternAnalyzer", "Run Script"))
        self.uploadData.setText(_translate("AntennaRadiationPatternAnalyzer", "Upload File Data"))
        self.exportData.setText(_translate("AntennaRadiationPatternAnalyzer", "Export Data"))
        self.changeView.setText(_translate("AntennaRadiationPatternAnalyzer", "Change View"))
        self.mapFrequency.setText(_translate("AntennaRadiationPatternAnalyzer", "Map Frequency"))
        self.frequencyInputLabel.setText(_translate("AntennaRadiationPatternAnalyzer", "Frequency Input:"))
        self.hz.setText(_translate("AntennaRadiationPatternAnalyzer", "Hz"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AntennaRadiationPatternAnalyzer = QtWidgets.QWidget()
    ui = Ui_AntennaRadiationPatternAnalyzer()
    ui.setupUi(AntennaRadiationPatternAnalyzer)
    AntennaRadiationPatternAnalyzer.show()
    sys.exit(app.exec())
