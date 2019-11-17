from tkinter import *
import instaloader
import config
from time import sleep


def login(driver):
    driver.get(config.INSTAGRAM_URL)
    sleep(3)
    username = driver.find_element_by_name('username')
    username.send_keys(config.USERNAME)
    password = driver.find_element_by_name('password')
    password.send_keys(config.PASSWORD)
    button_login = driver.find_element_by_css_selector(config.BUTTON_LOGIN)
    button_login.click()
    sleep(3)
    try:
        notnow = driver.find_element_by_css_selector(config.POPUP_NOTNOW)
        notnow.click()
    except Exception as e:
        if config.DEBUG:
            print(e)
        pass


class LoginForm:
    def __init__(self, master):
        self.master = master
        self.status = '                                                                          '
        self.username = ''
        self.password = ''

        topFrame = Frame(master)
        bottomFrame = Frame(master)
        footerFrame = Frame(master)

        topFrame.pack(expand=YES, side=TOP)
        bottomFrame.pack()
        footerFrame.pack(side=BOTTOM, fill=X)

        self.usernameLabel = Label(topFrame, text="Username")
        self.usernameEntry = Entry(topFrame)
        self.passwordLabel = Label(topFrame, text="Password")
        self.passwordEntry = Entry(topFrame, show="*")
        self.passwordEntry.bind("<Return>", self.check_credentials)

        self.usernameLabel.pack(padx=10)
        self.usernameEntry.pack(padx=10)
        self.passwordLabel.pack(padx=10)
        self.passwordEntry.pack(padx=10)

        self.loginButton = Button(bottomFrame, text="Login", command=self.check_credentials)
        self.loginButton.pack(padx=10, pady=10, side=LEFT)

        self.quitButton = Button(bottomFrame, text="Quit", command=self.quit_window)
        self.quitButton.pack(padx=10, pady=10, side=RIGHT)

        self.statusBar = Label(footerFrame, text=self.status, bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

    def get_user_info(self):
        self.username = self.usernameEntry.get()
        self.password = self.passwordEntry.get()

    def quit_window(self):
        self.master.destroy()

    def check_credentials(self, event=None):
        self.get_user_info()
        self.status_bar('Logging in...')
        try:
            L = instaloader.Instaloader()
            L.login(self.username, self.password)
            self.status_bar("Login Successful")
            sleep(2)
            config.USERNAME = self.username
            config.PASSWORD = self.password
            self.quit_window()
        except instaloader.exceptions.InvalidArgumentException as e:
            print(e)
            self.status_bar("User {} does not exist. Please Try Again!".format(self.username))
        except instaloader.exceptions.BadCredentialsException:
            self.status_bar("Incorrect Password. Please Try Again!")
        except Exception as e:
            print(e)
            exit()

    def status_bar(self, status):
        self.status = status
        self.statusBar.config(text=status)
        self.statusBar.update()
