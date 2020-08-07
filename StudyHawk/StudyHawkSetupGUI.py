# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\StudyHawk\StudyHawkSetupGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetupWindow(object):
    def setupUi(self, SetupWindow):
        SetupWindow.setObjectName("SetupWindow")
        SetupWindow.resize(800, 600)
        SetupWindow.setMinimumSize(QtCore.QSize(800, 600))
        SetupWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(SetupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, -80, 541, 661))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("background:qlineargradient(spread:pad, x1:0.937955, y1:1, x2:0, y2:0, stop:0 rgba(12, 72, 196, 255), stop:1 rgba(48, 255, 220, 255));\n"
"border-bottom-right-radius:40%;")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 451, 191))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size:70px;\n"
"color:white;\n"
"font-weight:bold;\n"
"")
        self.label.setObjectName("label")
        self.SetNameBTN = QtWidgets.QPushButton(self.centralwidget)
        self.SetNameBTN.setGeometry(QtCore.QRect(560, 420, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SetNameBTN.setFont(font)
        self.SetNameBTN.setStyleSheet("border-radius:25%;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(15, 0, 156, 255), stop:1 rgba(5, 224, 255, 255));\n"
"\n"
"color:white;")
        self.SetNameBTN.setObjectName("SetNameBTN")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(560, 350, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 300, 131, 41))
        self.label_2.setStyleSheet("font-size:25px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 550, 161, 21))
        self.label_3.setStyleSheet("font-size:20px;\n"
"background:transparent;\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, -1, 261, 271))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/StudyHawkLogo.png"))
        self.label_4.setObjectName("label_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 270, 421, 231))
        self.textBrowser_2.setStyleSheet("border:none;\n"
"background:transparent;\n"
"color:white;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.AboutUsBTN = QtWidgets.QPushButton(self.centralwidget)
        self.AboutUsBTN.setGeometry(QtCore.QRect(20, 500, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AboutUsBTN.setFont(font)
        self.AboutUsBTN.setStyleSheet("border-radius:25%;\n"
"background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(64, 64, 64, 255));\n"
"color:white;\n"
"")
        self.AboutUsBTN.setObjectName("AboutUsBTN")
        SetupWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SetupWindow)
        self.statusbar.setObjectName("statusbar")
        SetupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SetupWindow)
        QtCore.QMetaObject.connectSlotsByName(SetupWindow)

    def retranslateUi(self, SetupWindow):
        _translate = QtCore.QCoreApplication.translate
        SetupWindow.setWindowTitle(_translate("SetupWindow", "MainWindow"))
        self.label.setText(_translate("SetupWindow", "Welcome to\n"
"Study Hawk! "))
        self.SetNameBTN.setText(_translate("SetupWindow", "Yep, that\'\'s me!"))
        self.label_2.setText(_translate("SetupWindow", "First Name:"))
        self.label_3.setText(_translate("SetupWindow", " By Donald Lee"))
        self.textBrowser_2.setHtml(_translate("SetupWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#ffffff;\">To start, we will need your name! </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; color:#ffffff;\">This is because we will be calling you by your name when sending you notifications.</span></p></body></html>"))
        self.AboutUsBTN.setText(_translate("SetupWindow", "  About Study Hawk  "))
import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SetupWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
