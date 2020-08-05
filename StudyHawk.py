'''
StudyHawk by Donald Lee
Date: August 4th 2020

Installation:
pip install win10toast
'''

import time
from win10toast import ToastNotifier
import sys

Notify = ToastNotifier()

#Saves your name into a file
file = open("StudyHawkSavedData.txt", "a")
file = open("StudyHawkSavedData.txt", "r")
name = file.read()
#If your name is in the file, then you can now start being productive! :)
if len(name) > 0:
     file.close
#If your name is not in a file, we'll add your name to a file for you!
else:
    name = input("What's your name?: ")
    file = open("StudyHawkSavedData.txt", "w")
    file.write(name)
    file.close
    sys.exit("\nThanks " + name + "! " + "Your name has been saved in this program.\n\nPlease restart this program!")

#We will say hi to you!
print("\nHi " + name.strip() + "!\n")

#Sends you notifications when its time to rest or be productive
def beingproductive():

    time.sleep(int(productiveinseconds/2))
    Notify.show_toast("Study Hawk", "Halfway through! You better not be procrastinating " + name + "!", icon_path=None, duration=10)

    time.sleep(int(productiveinseconds/2 - 11))
    Notify.show_toast("Study Hawk", "Hi " + name + "! You can now take a " + str(round(rest)) + " minute break!", icon_path=None, duration=10)

    #Break time
    time.sleep(int(restinseconds/4 - 11))
    time.sleep(int(restinseconds/4))
    time.sleep(int(restinseconds/4))
    Notify.show_toast("Study Hawk", "Hi " + name + "! Your break is almost over!", icon_path=None, duration=10)

    time.sleep(int(restinseconds/4 - 6))
    Notify.show_toast("Study Hawk", "Hi " + name + "! Your " + str(round(rest)) + " minute break is over! Get back to work!", icon_path=None, duration=10)

    beingproductive()

while(1):
    try:
        minute = float(input("For how many minutes would you like to be productive for?: "))
        rest = float(input("How long in minutes would you like your breaks to be?: "))
        print("\nOk " + name + "! Good luck! \n\nPlease do not touch this program while it is running!")
        # Converts minutes to seconds
        productiveinseconds = minute * 60
        restinseconds = rest * 60

        # Runs the function called beingproductive
        beingproductive()
    except:
        print("\nError!\n")
        print("Please try again and ensure that your inputs only contains positive numbers and no letters or special characters!\n")
