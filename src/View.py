# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_CSV.ui'
#
# Created: Tue Jan 12 14:14:53 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(740, 575)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.out = QtGui.QTextBrowser(Form)
        self.out.setObjectName("out")
        self.gridLayout.addWidget(self.out, 0, 0, 1, 1)
        self.read = QtGui.QPushButton(Form)
        self.read.setObjectName("read")
        self.gridLayout.addWidget(self.read, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "CSVimportPython", None, QtGui.QApplication.UnicodeUTF8))
        self.read.setText(QtGui.QApplication.translate("Form", "CSV-File lesen", None, QtGui.QApplication.UnicodeUTF8))
