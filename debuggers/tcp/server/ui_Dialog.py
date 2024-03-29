# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 600)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidgetClients = QtWidgets.QListWidget(Dialog)
        self.listWidgetClients.setMinimumSize(QtCore.QSize(160, 80))
        self.listWidgetClients.setMaximumSize(QtCore.QSize(160, 16777215))
        self.listWidgetClients.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidgetClients.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetClients.setObjectName("listWidgetClients")
        self.gridLayout.addWidget(self.listWidgetClients, 4, 1, 1, 1)
        self.spinBoxPort = QtWidgets.QSpinBox(Dialog)
        self.spinBoxPort.setMinimumSize(QtCore.QSize(160, 27))
        self.spinBoxPort.setMaximumSize(QtCore.QSize(160, 27))
        self.spinBoxPort.setMinimum(1)
        self.spinBoxPort.setMaximum(65535)
        self.spinBoxPort.setProperty("value", 80)
        self.spinBoxPort.setObjectName("spinBoxPort")
        self.gridLayout.addWidget(self.spinBoxPort, 1, 1, 1, 1)
        self.checkBoxRawText = QtWidgets.QCheckBox(Dialog)
        self.checkBoxRawText.setObjectName("checkBoxRawText")
        self.gridLayout.addWidget(self.checkBoxRawText, 10, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEditTraffic = QtWidgets.QTextEdit(Dialog)
        self.textEditTraffic.setEnabled(False)
        self.textEditTraffic.setObjectName("textEditTraffic")
        self.verticalLayout.addWidget(self.textEditTraffic)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditData = LineEdit(Dialog)
        self.lineEditData.setEnabled(False)
        self.lineEditData.setObjectName("lineEditData")
        self.horizontalLayout.addWidget(self.lineEditData)
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSend.setFont(font)
        self.pushButtonSend.setAutoDefault(False)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.horizontalLayout.addWidget(self.pushButtonSend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 12, 1)
        self.labelClients = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelClients.setFont(font)
        self.labelClients.setObjectName("labelClients")
        self.gridLayout.addWidget(self.labelClients, 3, 1, 1, 1)
        self.labelFormat = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelFormat.setFont(font)
        self.labelFormat.setObjectName("labelFormat")
        self.gridLayout.addWidget(self.labelFormat, 7, 1, 1, 1)
        self.comboBoxFormat = QtWidgets.QComboBox(Dialog)
        self.comboBoxFormat.setMinimumSize(QtCore.QSize(160, 0))
        self.comboBoxFormat.setMaximumSize(QtCore.QSize(160, 16777215))
        self.comboBoxFormat.setObjectName("comboBoxFormat")
        self.comboBoxFormat.addItem("")
        self.comboBoxFormat.addItem("")
        self.comboBoxFormat.addItem("")
        self.comboBoxFormat.addItem("")
        self.gridLayout.addWidget(self.comboBoxFormat, 8, 1, 1, 1)
        self.labelPort = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPort.setFont(font)
        self.labelPort.setObjectName("labelPort")
        self.gridLayout.addWidget(self.labelPort, 0, 1, 1, 1)
        self.checkBoxLeadingZeroes = QtWidgets.QCheckBox(Dialog)
        self.checkBoxLeadingZeroes.setObjectName("checkBoxLeadingZeroes")
        self.gridLayout.addWidget(self.checkBoxLeadingZeroes, 9, 1, 1, 1)
        self.checkBoxTimestamp = QtWidgets.QCheckBox(Dialog)
        self.checkBoxTimestamp.setObjectName("checkBoxTimestamp")
        self.gridLayout.addWidget(self.checkBoxTimestamp, 11, 1, 1, 1)
        self.pushButtonStartStop = QtWidgets.QPushButton(Dialog)
        self.pushButtonStartStop.setMinimumSize(QtCore.QSize(160, 0))
        self.pushButtonStartStop.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonStartStop.setFont(font)
        self.pushButtonStartStop.setAutoDefault(False)
        self.pushButtonStartStop.setObjectName("pushButtonStartStop")
        self.gridLayout.addWidget(self.pushButtonStartStop, 2, 1, 1, 1)
        self.labelPeerAddress = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPeerAddress.setFont(font)
        self.labelPeerAddress.setObjectName("labelPeerAddress")
        self.gridLayout.addWidget(self.labelPeerAddress, 5, 1, 1, 1)
        self.lineEditPeerAddress = QtWidgets.QLineEdit(Dialog)
        self.lineEditPeerAddress.setMinimumSize(QtCore.QSize(160, 0))
        self.lineEditPeerAddress.setMaximumSize(QtCore.QSize(160, 16777215))
        self.lineEditPeerAddress.setReadOnly(True)
        self.lineEditPeerAddress.setObjectName("lineEditPeerAddress")
        self.gridLayout.addWidget(self.lineEditPeerAddress, 6, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButtonStartStop, self.lineEditData)
        Dialog.setTabOrder(self.lineEditData, self.pushButtonSend)
        Dialog.setTabOrder(self.pushButtonSend, self.spinBoxPort)
        Dialog.setTabOrder(self.spinBoxPort, self.comboBoxFormat)
        Dialog.setTabOrder(self.comboBoxFormat, self.checkBoxLeadingZeroes)
        Dialog.setTabOrder(self.checkBoxLeadingZeroes, self.checkBoxRawText)
        Dialog.setTabOrder(self.checkBoxRawText, self.checkBoxTimestamp)
        Dialog.setTabOrder(self.checkBoxTimestamp, self.textEditTraffic)
        Dialog.setTabOrder(self.textEditTraffic, self.listWidgetClients)
        Dialog.setTabOrder(self.listWidgetClients, self.lineEditPeerAddress)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TCP debugger (server) - 1.1.1"))
        self.checkBoxRawText.setText(_translate("Dialog", "Raw text"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
        self.labelClients.setText(_translate("Dialog", "Clients:"))
        self.labelFormat.setText(_translate("Dialog", "Format:"))
        self.comboBoxFormat.setItemText(0, _translate("Dialog", "Bin"))
        self.comboBoxFormat.setItemText(1, _translate("Dialog", "Oct"))
        self.comboBoxFormat.setItemText(2, _translate("Dialog", "Dec"))
        self.comboBoxFormat.setItemText(3, _translate("Dialog", "Hex"))
        self.labelPort.setText(_translate("Dialog", "Port:"))
        self.checkBoxLeadingZeroes.setText(_translate("Dialog", "Leading zeroes"))
        self.checkBoxTimestamp.setText(_translate("Dialog", "Timestamp"))
        self.pushButtonStartStop.setText(_translate("Dialog", "Start"))
        self.labelPeerAddress.setText(_translate("Dialog", "Peer address:"))

from debuggers.widgets import LineEdit
