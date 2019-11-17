from login import LoginForm
from instabotWindow import InstabotWindow
from tkinter import *
from sanitize import SanitaryTargets

# TODO UI with Current User Info
# Followings, Profile Pic, etc


def login():
    root = Tk()
    root.title(" Login")
    root.iconbitmap('assets/icon.ico')
    LoginForm(root)
    root.mainloop()


def choose():
    root = Tk()
    root.title(" InstaBot")
    root.iconbitmap('assets/icon.ico')
    InstabotWindow(root)
    root.mainloop()


if __name__ == '__main__':
    SanitaryTargets()
    login()
    choose()
