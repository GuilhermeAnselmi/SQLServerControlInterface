from tkinter import *
from tkinter import messagebox

from View.ssci import *

import json
import pymssql

class OpenConnect:
    def __init__(self, master=None):
        self.window = master
        self.window.title("SSCI - Connection")
        self.window.geometry("400x300+250+250")
        self.window.resizable(width=False, height=False)

        self.container = Frame(self.window)
        self.container.pack(side=TOP, padx=10, pady=10)

        self.content = LabelFrame(self.container, text="Connection", padx=5, pady=5)
        self.content.pack(side=TOP)

        self.lblHost = Label(self.content, text="Host")
        self.lblHost.grid(row=0, column=0)

        self.txtHost = Entry(self.content, width=29)
        self.txtHost.grid(row=1, column=0, columnspan=4)

        self.lblPort = Label(self.content, text="Port")
        self.lblPort.grid(row=0, column=4)

        self.txtPort = Entry(self.content, width=9)
        self.txtPort.grid(row=1, column=4, columnspan=2)

        self.space = Label(self.content)
        self.space.grid(row=2, column=0, columnspan=6)

        self.lblUser = Label(self.content, text="User")
        self.lblUser.grid(row=3, column=0)

        self.txtUser = Entry(self.content, width=19)
        self.txtUser.grid(row=4, column=0, columnspan=3, padx=3)

        self.lblPassword = Label(self.content, text="Password")
        self.lblPassword.grid(row=3, column=3)

        self.txtPassword = Entry(self.content, width=19, show="*")
        self.txtPassword.grid(row=4, column=3, columnspan=3, padx=3)

        self.checkboxs = Frame(self.container)
        self.checkboxs.pack(side=TOP, pady=5)

        connection = BooleanVar()
        self.ckbConnection = Checkbutton(self.checkboxs, text="Save Connection", var=connection)
        self.ckbConnection.grid(row=0, column=0)

        account = BooleanVar()
        self.ckbAccount = Checkbutton(self.checkboxs, text="Save Account", var=account)
        self.ckbAccount.grid(row=1, column=0)

        self.buttons = Frame(self.container)
        self.buttons.pack(side=BOTTOM, pady=5)

        self.btnDone = Button(self.buttons, text="Done", width=13)
        self.btnDone.bind("<ButtonRelease>", self.Exit)
        self.btnDone.grid(row=0, column=0, pady=3)

        self.btnConnect = Button(self.buttons, text="Connect", width=13)
        self.btnConnect.bind("<ButtonRelease>", self.Connect)
        self.btnConnect.grid(row=0, column=1, pady=3)

        self.btnTest = Button(self.buttons, text="Test Connection", width=13)
        self.btnTest.bind("<ButtonRelease>", self.Test)
        self.btnTest.grid(row=1, column=0, columnspan=2, pady=3)

    def Connect(self, event):
        try:
            conn = pymssql.connect(server=self.txtHost.get(),
                                   user=self.txtUser.get(),
                                   password=self.txtPassword.get(),
                                   port=self.txtPort.get(),
                                   database='master')

            verify = True
            ConnectionReady = True
        except:
            verify = False
            messagebox.showerror(title="Connection for SQL Server", message="Connection Refused")

        if verify:
            try:
                connection = {
                    "host": self.txtHost.get(),
                    "port": self.txtPort.get(),
                    "user": self.txtUser.get(),
                    "password": self.txtPassword.get()
                }

                with open("connections.json", "w") as f:
                    json.dump(connection, f)

                self.window.destroy()
            except:
                messagebox.showerror(title="Error", message="Could not create save file")

    def Test(self, event):
        try:
            conn = pymssql.connect(server=self.txtHost.get(),
                                   user=self.txtUser.get(),
                                   password=self.txtPassword.get(),
                                   port=self.txtPort.get(),
                                   database='master')

            messagebox.showinfo(title="Connection", message="Success!")
        except:
            messagebox.showerror(title="Connection Refused", message="Connection Refused")

        pass

    def Exit(self, event):
        self.window.destroy()

