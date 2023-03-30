# This file is for saving previous ui designs
# pyQt updates the antenna.py file with its own python code and deletes anything altered about it after running the command-
# pyuic6 -x AntennaAnalyze.ui -o antenna.py

import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from matplotlib import pyplot as plt
import random
import os
import re
import pyvisa as visa
import locale
import time
from PIL import Image
import math
from tempfile import NamedTemporaryFile

# global values
spinArray = []
spinsA = []
spinsE = []
grids = []


class Ui_AntennaRadiationPatternAnalyzer(object):

    def setupUi(self, AntennaRadiationPatternAnalyzer):

        # UI widet setup
        AntennaRadiationPatternAnalyzer.setObjectName("AntennaRadiationPatternAnalyzer")
        AntennaRadiationPatternAnalyzer.resize(1235, 600)
        AntennaRadiationPatternAnalyzer.setStyleSheet("")
        self.manualRunnerContainer_2 = QtWidgets.QFrame(AntennaRadiationPatternAnalyzer)
        self.manualRunnerContainer_2.setGeometry(QtCore.QRect(930, 70, 301, 461))
        self.manualRunnerContainer_2.setStyleSheet("background-color:rgb(211,211,211)")
        self.manualRunnerContainer_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.manualRunnerContainer_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.manualRunnerContainer_2.setObjectName("manualRunnerContainer_2")
        self.scriptElevation = QtWidgets.QLabel(self.manualRunnerContainer_2)
        self.scriptElevation.setGeometry(QtCore.QRect(70, 60, 151, 20))
        self.scriptElevation.setObjectName("scriptElevation")
        self.script_Runner = QtWidgets.QRadioButton(self.manualRunnerContainer_2)
        self.script_Runner.setEnabled(True)
        self.script_Runner.setGeometry(QtCore.QRect(80, 20, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        self.script_Runner.setFont(font)
        self.script_Runner.setChecked(False)
        self.script_Runner.setAutoExclusive(True)
        self.script_Runner.setObjectName("script_Runner")
        self.scriptAzmuth = QtWidgets.QLabel(self.manualRunnerContainer_2)
        self.scriptAzmuth.setGeometry(QtCore.QRect(70, 200, 151, 20))
        self.scriptAzmuth.setObjectName("scriptAzmuth")
        self.scriptStartSpinBox1 = QtWidgets.QSpinBox(self.manualRunnerContainer_2)
        self.scriptStartSpinBox1.setGeometry(QtCore.QRect(10, 120, 71, 22))
        self.scriptStartSpinBox1.setStyleSheet("background-color:rgb(255,255,255)")
        self.scriptStartSpinBox1.setObjectName("scriptStartSpinBox1")
        self.homeDevice2 = QtWidgets.QPushButton(self.manualRunnerContainer_2)
        self.homeDevice2.setGeometry(QtCore.QRect(70, 390, 141, 41))
        self.homeDevice2.setStyleSheet("QPushButton {background-color: black; color: white;}")
        self.homeDevice2.setObjectName("homeDevice2")
        self.run_script = QtWidgets.QPushButton(self.manualRunnerContainer_2)
        self.run_script.setGeometry(QtCore.QRect(80, 330, 121, 41))
        self.run_script.setStyleSheet("background-color:rgb(255,255,255)")
        self.run_script.setObjectName("run_script")
        self.scriptStopSpinBox1 = QtWidgets.QSpinBox(self.manualRunnerContainer_2)
        self.scriptStopSpinBox1.setGeometry(QtCore.QRect(110, 120, 71, 22))
        self.scriptStopSpinBox1.setStyleSheet("background-color:rgb(255,255,255)")
        self.scriptStopSpinBox1.setObjectName("scriptStopSpinBox1")
        self.scriptStartSpinBox2 = QtWidgets.QSpinBox(self.manualRunnerContainer_2)
        self.scriptStartSpinBox2.setGeometry(QtCore.QRect(10, 250, 71, 22))
        self.scriptStartSpinBox2.setStyleSheet("background-color:rgb(255,255,255)")
        self.scriptStartSpinBox2.setObjectName("scriptStartSpinBox2")
        self.scriptStopSpinBox2 = QtWidgets.QSpinBox(self.manualRunnerContainer_2)
        self.scriptStopSpinBox2.setGeometry(QtCore.QRect(110, 250, 71, 22))
        self.scriptStopSpinBox2.setStyleSheet("background-color:rgb(255,255,255)")
        self.scriptStopSpinBox2.setObjectName("scriptStopSpinBox2")
        self.scriptStepSize1 = QtWidgets.QSpinBox(self.manualRunnerContainer_2)
        self.scriptStepSize1.setGeometry(QtCore.QRect(210, 120, 71, 22))
        self.scriptStepSize1.setStyleSheet("background-color:rgb(255,255,255)")
        self.scriptStepSize1.setObjectName("scriptStepSize1")
        self.scriptStepSize2 = QtWidgets.QSpinBox(self.manualRunnerContainer_2)
        self.scriptStepSize2.setGeometry(QtCore.QRect(210, 250, 71, 22))
        self.scriptStepSize2.setStyleSheet("background-color:rgb(255,255,255)")
        self.scriptStepSize2.setObjectName("scriptStepSize2")
        self.scriptStart = QtWidgets.QLabel(self.manualRunnerContainer_2)
        self.scriptStart.setGeometry(QtCore.QRect(20, 90, 31, 20))
        self.scriptStart.setObjectName("scriptStart")
        self.scriptStop = QtWidgets.QLabel(self.manualRunnerContainer_2)
        self.scriptStop.setGeometry(QtCore.QRect(120, 90, 31, 20))
        self.scriptStop.setObjectName("scriptStop")
        self.scriptStepSize = QtWidgets.QLabel(self.manualRunnerContainer_2)
        self.scriptStepSize.setGeometry(QtCore.QRect(210, 90, 61, 20))
        self.scriptStepSize.setObjectName("scriptStepSize")
        self.buttonContainer = QtWidgets.QFrame(AntennaRadiationPatternAnalyzer)
        self.buttonContainer.setGeometry(QtCore.QRect(240, 540, 791, 61))
        self.buttonContainer.setStyleSheet("background-color:rgb(211,211,211)")
        self.buttonContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.buttonContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.buttonContainer.setObjectName("buttonContainer")
        self.uploadData = QtWidgets.QPushButton(self.buttonContainer)
        self.uploadData.setGeometry(QtCore.QRect(150, 10, 121, 41))
        self.uploadData.setStyleSheet("background-color:rgb(255,255,255)\n"
                                      "")
        self.uploadData.setObjectName("uploadData")
        self.exportData = QtWidgets.QPushButton(self.buttonContainer)
        self.exportData.setGeometry(QtCore.QRect(450, 10, 121, 41))
        self.exportData.setStyleSheet("background-color:rgb(255,255,255)")
        self.exportData.setObjectName("exportData")
        self.fruqencyMapContainer = QtWidgets.QFrame(AntennaRadiationPatternAnalyzer)
        self.fruqencyMapContainer.setGeometry(QtCore.QRect(240, 0, 791, 61))
        self.fruqencyMapContainer.setStyleSheet("background-color:rgb(211,211,211)")
        self.fruqencyMapContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fruqencyMapContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fruqencyMapContainer.setObjectName("fruqencyMapContainer")
        self.mapFrequency = QtWidgets.QPushButton(self.fruqencyMapContainer)
        self.mapFrequency.setGeometry(QtCore.QRect(640, 10, 121, 41))
        self.mapFrequency.setStyleSheet("background-color:rgb(255,255,255)")
        self.mapFrequency.setObjectName("mapFrequency")
        self.frequencyInputLabel = QtWidgets.QLabel(self.fruqencyMapContainer)
        self.frequencyInputLabel.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.frequencyInputLabel.setObjectName("frequencyInputLabel")
        self.hz = QtWidgets.QLabel(self.fruqencyMapContainer)
        self.hz.setGeometry(QtCore.QRect(230, 20, 58, 16))
        self.hz.setObjectName("hz")
        self.frequencyDropDown = QtWidgets.QComboBox(self.fruqencyMapContainer)
        self.frequencyDropDown.setGeometry(QtCore.QRect(120, 10, 103, 41))
        self.frequencyDropDown.setObjectName("frequencyDropDown")
        self.verticleAngles = QtWidgets.QRadioButton(self.fruqencyMapContainer)
        self.verticleAngles.setGeometry(QtCore.QRect(280, 10, 121, 20))
        self.verticleAngles.setObjectName("verticleAngles")
        self.horizontalAngles = QtWidgets.QRadioButton(self.fruqencyMapContainer)
        self.horizontalAngles.setGeometry(QtCore.QRect(280, 30, 131, 20))
        self.horizontalAngles.setObjectName("horizontalAngles")
        self.anglesDropDown = QtWidgets.QComboBox(self.fruqencyMapContainer)
        self.anglesDropDown.setGeometry(QtCore.QRect(470, 10, 103, 41))
        self.anglesDropDown.setObjectName("anglesDropDown")
        self.imagePlot = QtWidgets.QLabel(AntennaRadiationPatternAnalyzer)
        self.imagePlot.setGeometry(QtCore.QRect(330, 80, 571, 451))
        self.imagePlot.setText("")
        self.imagePlot.setObjectName("imagePlot")
        self.manualRunnerContainer_3 = QtWidgets.QFrame(AntennaRadiationPatternAnalyzer)
        self.manualRunnerContainer_3.setGeometry(QtCore.QRect(10, 70, 291, 461))
        self.manualRunnerContainer_3.setStyleSheet("background-color:rgb(211,211,211)")
        self.manualRunnerContainer_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.manualRunnerContainer_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.manualRunnerContainer_3.setObjectName("manualRunnerContainer_3")
        self.manualElevation = QtWidgets.QLabel(self.manualRunnerContainer_3)
        self.manualElevation.setGeometry(QtCore.QRect(70, 60, 151, 20))
        self.manualElevation.setObjectName("manualElevation")
        self.ManualRunner = QtWidgets.QRadioButton(self.manualRunnerContainer_3)
        self.ManualRunner.setEnabled(True)
        self.ManualRunner.setGeometry(QtCore.QRect(80, 20, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        self.ManualRunner.setFont(font)
        self.ManualRunner.setChecked(False)
        self.ManualRunner.setAutoExclusive(True)
        self.ManualRunner.setObjectName("ManualRunner")
        self.manualAzmuth = QtWidgets.QLabel(self.manualRunnerContainer_3)
        self.manualAzmuth.setGeometry(QtCore.QRect(70, 200, 151, 20))
        self.manualAzmuth.setObjectName("manualAzmuth")
        self.ManualStartSpinBox1 = QtWidgets.QSpinBox(self.manualRunnerContainer_3)
        self.ManualStartSpinBox1.setGeometry(QtCore.QRect(10, 120, 71, 22))
        self.ManualStartSpinBox1.setStyleSheet("background-color:rgb(255,255,255)")
        self.ManualStartSpinBox1.setObjectName("ManualStartSpinBox1")
        self.homeDevice1 = QtWidgets.QPushButton(self.manualRunnerContainer_3)
        self.homeDevice1.setGeometry(QtCore.QRect(70, 390, 141, 41))
        self.homeDevice1.setStyleSheet("QPushButton {background-color: black; color: white;}")
        self.homeDevice1.setObjectName("homeDevice1")
        self.manualStopSpinBox1 = QtWidgets.QSpinBox(self.manualRunnerContainer_3)
        self.manualStopSpinBox1.setGeometry(QtCore.QRect(110, 120, 71, 22))
        self.manualStopSpinBox1.setStyleSheet("background-color:rgb(255,255,255)")
        self.manualStopSpinBox1.setObjectName("manualStopSpinBox1")
        self.manualStartSpinBox2 = QtWidgets.QSpinBox(self.manualRunnerContainer_3)
        self.manualStartSpinBox2.setGeometry(QtCore.QRect(10, 250, 71, 22))
        self.manualStartSpinBox2.setStyleSheet("background-color:rgb(255,255,255)")
        self.manualStartSpinBox2.setObjectName("manualStartSpinBox2")
        self.manualStopSpinBox2 = QtWidgets.QSpinBox(self.manualRunnerContainer_3)
        self.manualStopSpinBox2.setGeometry(QtCore.QRect(110, 250, 71, 22))
        self.manualStopSpinBox2.setStyleSheet("background-color:rgb(255,255,255)")
        self.manualStopSpinBox2.setObjectName("manualStopSpinBox2")
        self.manualStepSize1 = QtWidgets.QSpinBox(self.manualRunnerContainer_3)
        self.manualStepSize1.setGeometry(QtCore.QRect(210, 120, 71, 22))
        self.manualStepSize1.setStyleSheet("background-color:rgb(255,255,255)")
        self.manualStepSize1.setObjectName("manualStepSize1")
        self.manualStepSize2 = QtWidgets.QSpinBox(self.manualRunnerContainer_3)
        self.manualStepSize2.setGeometry(QtCore.QRect(210, 250, 71, 22))
        self.manualStepSize2.setStyleSheet("background-color:rgb(255,255,255)")
        self.manualStepSize2.setObjectName("manualStepSize2")
        self.manualStart = QtWidgets.QLabel(self.manualRunnerContainer_3)
        self.manualStart.setGeometry(QtCore.QRect(20, 90, 41, 20))
        self.manualStart.setObjectName("manualStart")
        self.manualStop = QtWidgets.QLabel(self.manualRunnerContainer_3)
        self.manualStop.setGeometry(QtCore.QRect(120, 90, 51, 20))
        self.manualStop.setObjectName("manualStop")
        self.manualStepSize = QtWidgets.QLabel(self.manualRunnerContainer_3)
        self.manualStepSize.setGeometry(QtCore.QRect(220, 90, 61, 20))
        self.manualStepSize.setObjectName("manualStepSize")

        # initial state
        self.frequenciesDropDown(self.frequencyDropDown, [])
        self.script_Runner.setChecked(True)
        self.disableManual(self.ManualRunner, self.script_Runner, self.ManualStartSpinBox1, self.manualStopSpinBox1,
                           self.manualStartSpinBox2, self.manualStopSpinBox2, self.manualStepSize1,
                           self.manualStepSize2,
                           self.homeDevice1, self.scriptStartSpinBox1, self.scriptStopSpinBox1,
                           self.scriptStartSpinBox2, self.scriptStopSpinBox2, self.scriptStepSize1,
                           self.scriptStepSize2,
                           self.homeDevice2, self.run_script)
        self.scriptStartSpinBox1.setRange(-90, 90)
        self.scriptStartSpinBox2.setRange(-90, 90)
        self.scriptStopSpinBox2.setRange(-90, 90)
        self.scriptStopSpinBox1.setRange(-90, 90)
        # function calls
        self.mapFrequency.clicked.connect(self.plot)
        self.homeDevice1.clicked.connect(self.homedevice)
        self.homeDevice2.clicked.connect(self.homedevice)
        self.run_script.clicked.connect(self.runScript)
        self.ManualStartSpinBox1.setRange(0, 90)
        self.ManualRunner.toggled.connect(
            lambda: self.disableManual(self.ManualRunner, self.script_Runner, self.ManualStartSpinBox1,
                                       self.manualStopSpinBox1,
                                       self.manualStartSpinBox2, self.manualStopSpinBox2, self.manualStepSize1,
                                       self.manualStepSize2,
                                       self.homeDevice1, self.scriptStartSpinBox1, self.scriptStopSpinBox1,
                                       self.scriptStartSpinBox2, self.scriptStopSpinBox2, self.scriptStepSize1,
                                       self.scriptStepSize2,
                                       self.homeDevice2, self.run_script))
        self.script_Runner.toggled.connect(
            lambda: self.disableScript(self.ManualRunner, self.script_Runner, self.scriptStartSpinBox1,
                                       self.scriptStopSpinBox1, self.scriptStartSpinBox2, self.scriptStopSpinBox2,
                                       self.scriptStepSize1,
                                       self.scriptStepSize2, self.homeDevice2,
                                       self.ManualStartSpinBox1, self.manualStopSpinBox1,
                                       self.manualStartSpinBox2, self.manualStopSpinBox2, self.manualStepSize1,
                                       self.manualStepSize2,
                                       self.homeDevice1, self.run_script))

        self.uploadData.clicked.connect(self.uploadFiles)
        self.scriptStartSpinBox1.valueChanged.connect(lambda: self.getSpinValue(self.scriptStartSpinBox1, 1))
        self.scriptStopSpinBox1.valueChanged.connect(lambda: self.getSpinValue(self.scriptStopSpinBox1, 2))
        self.scriptStepSize1.valueChanged.connect(lambda: self.getSpinValue(self.scriptStepSize1, 3))
        self.scriptStartSpinBox2.valueChanged.connect(lambda: self.getSpinValue(self.scriptStartSpinBox2, 4))
        self.scriptStopSpinBox2.valueChanged.connect(lambda: self.getSpinValue(self.scriptStopSpinBox2, 5))
        self.scriptStepSize2.valueChanged.connect(lambda: self.getSpinValue(self.scriptStepSize2, 6))
        self.run_script.setStyleSheet("border-radius : 50; border: 2px solid black")

        self.retranslateUi(AntennaRadiationPatternAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(AntennaRadiationPatternAnalyzer)

    def sweep(self):

        # initilize

        SCPI_server_IP = '169.254.45.134'
        SCPI_Port = '5025'
        SCPI_timeout = 20000  # milliseconds
        VISA_resource_name = 'TCPIP::' + SCPI_server_IP + '::' + SCPI_Port + '::SOCKET'
        visaSession = visa.ResourceManager().open_resource(VISA_resource_name)
        visaSession.timeout = SCPI_timeout
        visaSession.read_termination = '\n'
        visaSession.write('INIT:CONT 0')
        visaSession.write('INITiate:IMMediate')
        visaSession.write('CALC:PAR:DEF S21')

        frequencyValues = visaSession.query(":SENS:FREQ:DATA?")
        frequencyValues_list = list(map(float, frequencyValues.split(",")))

        for i in range(0, len(frequencyValues_list)):
            frequencyValues_list[i] = frequencyValues_list[i] / (10 ** 9)

        self.buildArrays(spinsA, spinsE, len(frequencyValues_list))

        finish = visaSession.query(
            '*OPC?')  # this command waits for all pending operations to finish and afterwards returns an 1

        numrows = len(grids[0])
        numcols = len(grids[0][0])
        Matrix = [[0 for x in range(numcols)] for y in range(numrows)]
        counter = 0
        for i in range(0, numrows):
            if (counter == 0):
                for j in range(0, numcols):
                    magnitudes = self.magnitudes(visaSession)
                    for k in range(0, len(magnitudes)):
                        grids[k][i][j] = magnitudes[k]

            if (counter == 1):
                for j in range(numcols - 1, -1, -1):
                    magnitudes = self.magnitudes(visaSession)
                    for k in range(0, len(magnitudes)):
                        grids[k][i][j] = magnitudes[k]
            counter = (counter + 1) % 2
        for i in range(0, len(frequencyValues_list)):
            place = i + 1
            print("Frequency " + str(place) + ": " + str(frequencyValues_list[i]))
            grid = grids[i]
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))


        visaSession.close()

    def magnitudes(self, visaSession):
        allResults = visaSession.query(":CALC:DATA:SDAT?")
        allResults_list = list(map(float, allResults.split(",")))
        magnitudesList = []
        for i in range(0, len(allResults_list), 2):
            magnitude = allResults_list[i] ** 2 + allResults_list[i + 1] ** 2
            magnitude = magnitude ** .5
            magnitudesList.append(magnitude)
        return magnitudesList

    def frequenciesDropDown(self, frequencydrop, frequencyarray):
        frequencyarray = [1,3,4,5]
        if len(frequencyarray) != 0:
            for i in range(0,len(frequencyarray)):
                print(i)
                frequencydrop.addItem(str(frequencyarray[i]))

    def angleDropDownVerticle(self, angledrop, anglearray):
        for i in anglearray:
            angledrop.addItem(str(i))



    def homedevice(self):
        msg = QMessageBox()
        msg.setWindowTitle("Pop Up")
        msg.setText("homing device")
        msg.exec()

    def checkstepSizeElevation(self, Startvalue1, Stopvalue1, Stepvalue1):
        if ((abs(Stopvalue1 - Startvalue1) % Stepvalue1) != 0):
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Change start, stop, or step value in elevation inputs as this is not a valid number of steps")

            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            return False
        return True

    def checkstepSizeAzmuth(self, Startvalue2, Stopvalue2, Stepvalue2):
        if ((abs(Stopvalue2 - Startvalue2) % Stepvalue2) != 0):
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Change start, stop, or step value in azmuth inputs as this is not a valid number of steps")

            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            return False
        return True

    def checkForZero(self, stepValue):
        if (stepValue == 0):
            return False
        return True

    def runScript(self):
        global spinsA
        global spinsE
        spinsE.clear()
        spinsA.clear()

        if (
                self.scriptStepSize1.value() == 0 and self.scriptStartSpinBox1.value() == 0 and self.scriptStopSpinBox1.value() == 0 and self.scriptStepSize2.value() == 0 and self.scriptStartSpinBox2.value() == 0 and self.scriptStopSpinBox2.value() == 0):
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("put in some value")

            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            return
        if self.scriptStepSize1.value() > 0 and self.scriptStartSpinBox1.value() == 0 and self.scriptStopSpinBox1.value() == 0:
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Cannot have more than 1 step size while not having start or stop in elevation plane")

            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            return
        if self.scriptStepSize2.value() > 0 and self.scriptStartSpinBox2.value() == 0 and self.scriptStopSpinBox2.value() == 0:
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Cannot have more than 1 step size while not having start or stop in azmuth plane")

            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            return
        if  self.scriptStartSpinBox2.value() > self.scriptStopSpinBox2.value():
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Cannot have a start greater than the stop in azmuth plane")

            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            return
        if  self.scriptStartSpinBox1.value() > self.scriptStopSpinBox1.value():
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Cannot have a start greater than the stop in elevation plane")

            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            return
        if (
                self.scriptStartSpinBox1.value() > 0 or self.scriptStartSpinBox1.value() < 0 or self.scriptStopSpinBox1.value() > 0 or self.scriptStopSpinBox1.value() < 0):
            if (self.checkForZero(self.scriptStepSize1.value())):
                if (self.checkstepSizeElevation(self.scriptStartSpinBox1.value(), self.scriptStopSpinBox1.value(),
                                                self.scriptStepSize1.value())):
                    spinsE.append(self.scriptStartSpinBox1.value())
                    spinsE.append(self.scriptStopSpinBox1.value())
                    spinsE.append(self.scriptStepSize1.value())
                else:
                    return

            else:
                msg = QMessageBox()

                msg.setWindowTitle("Error")
                msg.setText("Cannot have 0 step size in elevation plane")

                msg.setIcon(QMessageBox.Icon.Critical)
                msg.exec()
                return
        if (self.scriptStartSpinBox2.value() > 0 or self.scriptStartSpinBox2.value() < 0 or self.scriptStopSpinBox2.value() > 0 or self.scriptStopSpinBox2.value() < 0):
            if (self.checkForZero(self.scriptStepSize2.value())):
                if (self.checkstepSizeAzmuth(self.scriptStartSpinBox2.value(), self.scriptStopSpinBox2.value(),
                                             self.scriptStepSize2.value())):
                    spinsA.append(self.scriptStartSpinBox2.value())
                    spinsA.append(self.scriptStopSpinBox2.value())
                    spinsA.append(self.scriptStepSize2.value())
                else:
                    return

            else:
                msg = QMessageBox()

                msg.setWindowTitle("Error")
                msg.setText("Cannot have 0 step size in azmuth plane")

                msg.setIcon(QMessageBox.Icon.Critical)
                msg.exec()
                return
        if (len(spinsA) == 0):
            spinsA.append(0)
            spinsA.append(0)
            spinsA.append(0)
        if (len(spinsE) == 0):
            spinsE.append(0)
            spinsE.append(0)
            spinsE.append(0)
        print(spinsA)
        print("\n")
        print(spinsE)
        elevationArray = []
        elevationArray.clear()
        self.anglesDropDown.clear()
        print(self.anglesDropDown.itemData(0))
        for i in range(( spinsE[0]), (spinsE[1])+1, spinsE[2]):
            elevationArray.append(i)
        self.angleDropDownVerticle(self.anglesDropDown, elevationArray)
        self.sweep()

    def buildArrays(self, spinsA, spinsE, tracePoints):
        global grids
        grids = []
        rows = (spinsA[1] - spinsA[0]) / spinsA[2]
        columns = (spinsE[1] - spinsE[0]) / spinsE[2]
        for i in range(0, tracePoints):
            grids.append([[0 for x in range(int(columns))] for y in range(int(rows))])

        # for array in grids:
        #     print(array)
        #     print("*********************")

    def parseFrequencies(self):
        global spinArray
        f = open("graph1.txt", "r", encoding='utf-16')
        data = f.read()
        counter = 0
        values = ""
        for char in data:
            if counter == 2:
                if char == ']':
                    counter += 1
                    break
                values += char

            if char == '[':
                counter += 1
        values = ''.join(values.splitlines())
        frequencies = values.split()
        counter = 0
        for value in frequencies:
            number = ''.join(x for x in value if x.isdigit())
            base = number[0] + '.' + number[1:9]
            print(base)
            power = number[9:]
            base = float(base)
            power = int(power)
            frequencies[counter] = round((base * (10 ** power)) / (10 ** 9), 2)
            counter += 1
        print(frequencies)
        spinArray = frequencies
        self.sweep()

        """
        start = "["
        end = "]"
        print((data.split(start))[1].split(end)[0])
        """
        """
        for line in data:
            if 'Number' in line:
                wholeLine = line.strip()
                tracePoints = ''.join(x for x in wholeLine if x.isdigit())
        """

    def parseTracePoints(self):
        f = open("graph1.txt", "r", encoding='utf-16')
        data = f.readlines()
        for line in data:
            if 'Number' in line:
                wholeLine = line.strip()
                tracePoints = ''.join(x for x in wholeLine if x.isdigit())
        return tracePoints

    def plot(self):
        r = np.arange(spinsE[0], spinsE[1], spinsE[2])
        theta = grids[2][1]

        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.plot(r, theta)
        ax.set_rmax(.003)
        # ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
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

    def disableManual(self, radioButton1, radioButton2, startSpin1, stopSpin1, startSpin2, stopSpin2, stepSize1,
                      stepSize2, homedevice1, startSpin3, stopSpin3, startSpin4, stopSpin4, stepSize3, stepSize4,
                      homedevice2, runScript):
        print("script runner mode initiated")
        radioButton1.setEnabled(False)
        startSpin1.setEnabled(False)
        stopSpin1.setEnabled(False)
        startSpin2.setEnabled(False)
        stopSpin2.setEnabled(False)
        stepSize1.setEnabled(False)
        stepSize2.setEnabled(False)
        homedevice1.setEnabled(False)

        radioButton2.setEnabled(True)
        radioButton1.setEnabled(False)
        startSpin3.setEnabled(True)
        stopSpin3.setEnabled(True)
        startSpin4.setEnabled(True)
        stopSpin4.setEnabled(True)
        stepSize3.setEnabled(True)
        stepSize4.setEnabled(True)
        homedevice2.setEnabled(True)
        runScript.setEnabled(True)

    def disableScript(self, radioButton1, radioButton2, startSpin1, stopSpin1, startSpin2, stopSpin2, stepSize1,
                      stepSize2, homedevice2, startSpin3, stopSpin3, startSpin4, stopSpin4, stepSize3, stepSize4,
                      homedevice1, runScript):
        print("manual runner mode initiated")
        radioButton1.setEnabled(False)
        startSpin1.setEnabled(False)
        stopSpin1.setEnabled(False)
        startSpin2.setEnabled(False)
        stopSpin2.setEnabled(False)
        stepSize1.setEnabled(False)
        stepSize2.setEnabled(False)
        homedevice2.setEnabled(False)
        runScript.setEnabled(False)

        radioButton1.setEnabled(True)
        radioButton2.setEnabled(False)
        startSpin3.setEnabled(True)
        stopSpin3.setEnabled(True)
        startSpin4.setEnabled(True)
        stopSpin4.setEnabled(True)
        stepSize3.setEnabled(True)
        stepSize4.setEnabled(True)
        homedevice1.setEnabled(True)

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

    def getSpinValue(self, spinbox, val):
        if (val == 1):
            value = spinbox.value()
            print("startspinbox:", value)
        if (val == 2):
            value2 = spinbox.value()
            print("stopspinbox:", value2)
        if (val == 3):
            value3 = spinbox.value()
            print("stepsizebox:", value3)
        if (val == 4):
            value4 = spinbox.value()
            print("startspinbox:", value4)
        if (val == 5):
            value5 = spinbox.value()
            print("stopspinbox:", value5)
        if (val == 6):
            value6 = spinbox.value()
            print("stepsizebox:", value6)

    def retranslateUi(self, AntennaRadiationPatternAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        AntennaRadiationPatternAnalyzer.setWindowTitle(_translate("AntennaRadiationPatternAnalyzer", "Widget"))
        self.scriptElevation.setText(_translate("AntennaRadiationPatternAnalyzer", "              Elevation"))
        self.script_Runner.setText(_translate("AntennaRadiationPatternAnalyzer", "  Script Runner"))
        self.scriptAzmuth.setText(_translate("AntennaRadiationPatternAnalyzer", "              Azmuth"))
        self.homeDevice2.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))
        self.run_script.setText(_translate("AntennaRadiationPatternAnalyzer", "Run Script"))
        self.scriptStart.setText(_translate("AntennaRadiationPatternAnalyzer", "Start"))
        self.scriptStop.setText(_translate("AntennaRadiationPatternAnalyzer", "Stop"))
        self.scriptStepSize.setText(_translate("AntennaRadiationPatternAnalyzer", "Step Size"))
        self.uploadData.setText(_translate("AntennaRadiationPatternAnalyzer", "Upload File Data"))
        self.exportData.setText(_translate("AntennaRadiationPatternAnalyzer", "Export Data"))
        self.mapFrequency.setText(_translate("AntennaRadiationPatternAnalyzer", "Map Frequency"))
        self.frequencyInputLabel.setText(_translate("AntennaRadiationPatternAnalyzer", "Frequency Input:"))
        self.hz.setText(_translate("AntennaRadiationPatternAnalyzer", "Hz"))
        self.verticleAngles.setText(_translate("AntennaRadiationPatternAnalyzer", "Verticle Angles"))
        self.horizontalAngles.setText(_translate("AntennaRadiationPatternAnalyzer", "Horizontal Angles"))
        self.manualElevation.setText(_translate("AntennaRadiationPatternAnalyzer", "              Elevation"))
        self.ManualRunner.setText(_translate("AntennaRadiationPatternAnalyzer", "Manual Runner"))
        self.manualAzmuth.setText(_translate("AntennaRadiationPatternAnalyzer", "              Azmuth"))
        self.homeDevice1.setText(_translate("AntennaRadiationPatternAnalyzer", "Home Device"))
        self.manualStart.setText(_translate("AntennaRadiationPatternAnalyzer", "Start"))
        self.manualStop.setText(_translate("AntennaRadiationPatternAnalyzer", "Stop"))
        self.manualStepSize.setText(_translate("AntennaRadiationPatternAnalyzer", "Step Size"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AntennaRadiationPatternAnalyzer = QtWidgets.QWidget()
    ui = Ui_AntennaRadiationPatternAnalyzer()
    ui.setupUi(AntennaRadiationPatternAnalyzer)
    AntennaRadiationPatternAnalyzer.show()
    sys.exit(app.exec())