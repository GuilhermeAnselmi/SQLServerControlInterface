from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from Control.config import *


class Settings:
    def __init__(self, master=None):
        self.master = master
        self.master.geometry("700x455+250+250")
        self.master.resizable(width=False, height=False)

        self.window = Frame(self.master)
        self.window.pack(side=TOP, fill="both")

        #Lateral Menu
        self.list = Frame(self.window, bg="black")
        self.list.pack(side=LEFT, fill="y", expand=False, anchor="w")

        self.lstMenu = Listbox(self.list, height=25)
        self.lstMenu.pack(side=LEFT, anchor="w")
        self.lstMenu.insert(0, "Theme")
        self.lstMenu.insert(1, "Teste")
        self.lstMenu.bind("<<ListboxSelect>>", self.ContentSettings)

        #Buttons
        self.buttons = Frame(self.window)
        self.buttons.pack(side=BOTTOM, fill="x", padx=10, pady=10)

        self.btnDone = Button(self.buttons, text="Done")
        self.btnDone.bind("<ButtonRelease>", self.Done)
        self.btnDone.pack(side=LEFT)

        self.btnSave = Button(self.buttons, text="Save", state="disabled")
        self.btnSave.bind("<ButtonRelease>", self.Save)
        self.btnSave.pack(side=RIGHT)

        #Theme Settings
        self.theme = Frame(self.window)

        self.options = Frame(self.theme)
        self.options.pack(side=TOP)

        self.cbbTheme = Combobox(self.options, values=["Dark", "Light"], state="readonly")
        self.cbbTheme.current(0)
        self.cbbTheme.grid(row=0, column=0)

    def ContentSettings(self, event):
        index = self.lstMenu.curselection()[0]
        self.btnSave['state'] = NORMAL

        if index == 0:
            self.theme.pack(side=RIGHT, fill="both", expand=True, anchor="center", pady=10, padx=10)
        else:
            self.theme.pack_forget()
            self.btnSave['state'] = DISABLED

    def Save(self, event):
        verify = Config().Save(theme=self.cbbTheme.get())

        if verify:
            messagebox.showinfo(title="Saved Successfully", message="Settings have been saved")
        else:
            messagebox.showerror(title="Error", message="Error saving settings")

    def Done(self, event):
        self.master.destroy()
