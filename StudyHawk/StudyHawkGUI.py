# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\StudyHawk\StudyHawkTimerUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 770)
        MainWindow.setMinimumSize(QtCore.QSize(860, 643))
        MainWindow.setMaximumSize(QtCore.QSize(860, 6430))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Productivevalue = QtWidgets.QSpinBox(self.centralwidget)
        self.Productivevalue.setGeometry(QtCore.QRect(40, 270, 171, 101))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.Productivevalue.setFont(font)
        self.Productivevalue.setMinimum(5)
        self.Productivevalue.setMaximum(1440)
        self.Productivevalue.setSingleStep(5)
        self.Productivevalue.setProperty("value", 5)
        self.Productivevalue.setObjectName("Productivevalue")
        self.Breakvalue = QtWidgets.QSpinBox(self.centralwidget)
        self.Breakvalue.setGeometry(QtCore.QRect(40, 500, 171, 91))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(40)
        self.Breakvalue.setFont(font)
        self.Breakvalue.setMinimum(1)
        self.Breakvalue.setMaximum(120)
        self.Breakvalue.setObjectName("Breakvalue")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 170, 501, 81))
        self.textBrowser.setStyleSheet("background: white;\n"
"border-bottom-right-radius:35%;\n"
"border-top-right-radius:35%;")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-110, -90, 1021, 1131))
        self.label.setMinimumSize(QtCore.QSize(1021, 1131))
        self.label.setMaximumSize(QtCore.QSize(10210, 11310))
        self.label.setStyleSheet("background:url(:/newPrefix/StudyHawkBg.png)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 10, 261, 271))
        self.label_2.setStyleSheet("background: url(:/newPrefix/StudyHawkLogo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(40, 400, 431, 81))
        self.textBrowser_3.setStyleSheet("background: white;\n"
"border-bottom-right-radius:35%;\n"
"border-top-right-radius:35%;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 20, 651, 131))
        self.textBrowser_2.setStyleSheet("background: transparent;\n"
"color:white;\n"
"border:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(0, 710, 211, 41))
        self.textBrowser_4.setStyleSheet("background: white;\n"
"color:black;\n"
"border:none;\n"
"border-top-right-radius:35%;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.GitHubLinkButton = QtWidgets.QPushButton(self.centralwidget)
        self.GitHubLinkButton.setGeometry(QtCore.QRect(510, 710, 351, 41))
        self.GitHubLinkButton.setStyleSheet("background:white;\n"
"border:none;\n"
"color:black;\n"
"font-size:16px;\n"
"border-top-left-radius:35%;")
        self.GitHubLinkButton.setObjectName("GitHubLinkButton")
        self.ready = QtWidgets.QPushButton(self.centralwidget)
        self.ready.setGeometry(QtCore.QRect(290, 590, 291, 101))
        font = QtGui.QFont()
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.ready.setFont(font)
        self.ready.setStyleSheet("border-radius:20%;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(15, 0, 156, 255), stop:1 rgba(5, 224, 255, 255));\n"
"color:white;\n"
"font-weight:bold;")
        self.ready.setObjectName("ready")
        self.ChangeName = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeName.setGeometry(QtCore.QRect(630, 310, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ChangeName.setFont(font)
        self.ChangeName.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(15, 0, 156, 255), stop:1 rgba(5, 224, 255, 255));\n"
"color:white;\n"
"font-weight:bold;\n"
"border-bottom-left-radius:35%;\n"
"border-top-left-radius:35%;")
        self.ChangeName.setObjectName("ChangeName")
        self.label.raise_()
        self.label_2.raise_()
        self.Productivevalue.raise_()
        self.Breakvalue.raise_()
        self.textBrowser.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser_4.raise_()
        self.GitHubLinkButton.raise_()
        self.ready.raise_()
        self.ChangeName.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:600;\">For how many minutes would you like to be productive for?</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:600; color:#000000;\">How long in minutes would you like your breaks to be?</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:72pt; font-weight:600;\">Study Hawk</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">© 2020 Donald Lee</span></p></body></html>"))
        self.GitHubLinkButton.setText(_translate("MainWindow", "https://github.com/Donald-K-Lee/StudyHawk"))
        self.ready.setText(_translate("MainWindow", "I\'m Ready!"))
        self.ChangeName.setText(_translate("MainWindow", "Change Name"))
import Bg_rc
import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())