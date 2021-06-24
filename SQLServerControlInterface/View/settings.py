from tkinter import *
from tkinter import messagebox

class Settings:
    def __init__(self, master=None):
        self.master = master
        self.master.geometry("700x455+250+250")
        self.master.resizable(width=False, height=False)

        self.window = Frame(self.master)
        self.window.pack(side=TOP, fill="both")

        #Lateral Menu
        self.list = Frame(self.window, bg="black")
        self.list.pack(side=LEFT, fill="y", expand=True, anchor="w")

        self.lstMenu = Listbox(self.list, height=25)
        self.lstMenu.pack(side=LEFT, anchor="w")
        self.lstMenu.insert(1, "Python")
