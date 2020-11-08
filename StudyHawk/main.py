'''
StudyHawk by Donald Lee
Date: August 4th-7th 2020

Installation:
pip install win10toast
pip install PyQt5
'''

from StudyHawkGUI import *
from StudyHawkSetupGUI import *
import sys
import webbrowser
import time
from win10toast import ToastNotifier

Notify = ToastNotifier()

while(1):
    try:
        #Sends you notifications when its time to rest or be productive
        def beingproductive():
            time.sleep(int(productiveinseconds/2))
            Notify.show_toast("Study Hawk", "Halfway through! You better not be procrastinating " + name + "!", icon_path="StudyHawkLogo.ico", duration=0)

            time.sleep(int(productiveinseconds/2))
            Notify.show_toast("Study Hawk", "Hi " + name + "! You can now take a " + str(round(rest)) + " minute break!", icon_path="StudyHawkLogo.ico", duration=0)

            #Break time
            time.sleep(int(restinseconds/4))
            time.sleep(int(restinseconds/4))
            time.sleep(int(restinseconds/4))
            Notify.show_toast("Study Hawk", "Hi " + name + "! Your break is almost over!", icon_path="StudyHawkLogo.ico", duration=0)
            time.sleep(int(restinseconds/4))
            Notify.show_toast("Study Hawk", "Hi " + name + "! Your " + str(round(rest)) + " minute break is over! Get back to work!", icon_path="StudyHawkLogo.ico", duration=0)
            beingproductive()

        class GUI(Ui_MainWindow):
            def __init__(self, window):
                self.setupUi(window)
                #Links the GUI to code
                self.ready.clicked.connect(self.getValue)
                self.GitHubLinkButton.clicked.connect(self.openGitHub)
                self.ChangeName.clicked.connect(self.ResetName)

            def openGitHub(self):
                webbrowser.open("https://github.com/Donald-K-Lee/StudyHawk")
            def ResetName(self):
                global name
                global file
                Notify.show_toast("Study Hawk", "Your name has been deleted! Please restart this program!",icon_path="StudyHawkLogo.ico", duration=0)
                file = open("StudyHawkSavedData.txt", "w")
                file.close()
                sys.exit()

            def getValue(self):
                global productiveinseconds
                global restinseconds
                global rest

                minute = self.Productivevalue.value()
                rest = self.Breakvalue.value()
                # Converts minutes to seconds
                productiveinseconds = minute * 60
                restinseconds = rest * 60
                Notify.show_toast("Study Hawk", "Got it! Please minimize this program and DO NOT touch it at ALL! Doing so can result in it crashing!",icon_path="StudyHawkLogo.ico", duration=0)
                Notify.show_toast("Study Hawk", "Got it! Please minimize this program and DO NOT touch it at ALL! Doing so can result in it crashing!",icon_path="StudyHawkLogo.ico", duration=0)
                beingproductive()

        class Setup(Ui_SetupWindow):
            def __init__(self, window):
                self.setupUi(window)
                # Links the GUI to code
                self.SetNameBTN.clicked.connect(self.setname)
                self.AboutUsBTN.clicked.connect(self.openGitHub)

            def openGitHub(self):
                webbrowser.open("https://github.com/Donald-K-Lee/StudyHawk")

            def setname(self):
                global file
                name = self.lineEdit.text()
                #Saves your name in a file
                file = open("StudyHawkSavedData.txt", "a")
                file = open("StudyHawkSavedData.txt", "w")
                file.write(name)
                file.close()
                if len(name) > 0:
                    Notify.show_toast("Study Hawk", "Thank you " + name + "! Please restart this program!",icon_path="StudyHawkLogo.ico", duration=0)
                    sys.exit()
                else:
                    Notify.show_toast("Study Hawk", "You did not enter your name! Please restart this program!",icon_path="StudyHawkLogo.ico", duration=0)
                    sys.exit()

        file = open("StudyHawkSavedData.txt", "a")
        file = open("StudyHawkSavedData.txt", "r")
        name = file.read()
        #If name in file
        if len(name) > 0:
             file.close()
             app = QtWidgets.QApplication(sys.argv)
             MainWindow = QtWidgets.QMainWindow()

             ui = GUI(MainWindow)

             # Opens the GUI
             MainWindow.show()
             app.exec_()

        #If your name is not in a file, we'll add your name to a file for you!
        else:
            app = QtWidgets.QApplication(sys.argv)
            SetupWindow = QtWidgets.QMainWindow()

            Setupui = Setup(SetupWindow)

            # Opens the GUI
            SetupWindow.show()
            app.exec_()
    except:
        Notify.show_toast("Study Hawk", "Error, please try again!",icon_path="StudyHawkLogo.ico", duration=10)

