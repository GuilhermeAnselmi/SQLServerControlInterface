from tkinter import *
from tkinter import messagebox

from Control.conn import *

import os.path

class OpenConnect:
    def __init__(self, master=None, session=None):
        self.window = master
        self.window.title("SSCI - Connection")
        self.window.geometry("400x300+250+250")
        self.window.resizable(width=False, height=False)

        self.session = session

        #Frame Master
        self.container = Frame(self.window)
        self.container.pack(side=TOP, padx=10, pady=10)

        #Connections Info
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

        if os.path.isfile("connection.json"):
            connect = RequestConn()
            self.txtHost.insert(0, connect['host'])
            self.txtPort.insert(0, connect['port'])

        self.space = Label(self.content)
        self.space.grid(row=2, column=0, columnspan=6)

        #Accounts Info
        self.lblUser = Label(self.content, text="User")
        self.lblUser.grid(row=3, column=0)

        self.txtUser = Entry(self.content, width=19)
        self.txtUser.grid(row=4, column=0, columnspan=3, padx=3)

        self.lblPassword = Label(self.content, text="Password")
        self.lblPassword.grid(row=3, column=3)

        self.txtPassword = Entry(self.content, width=19, show="*")
        self.txtPassword.grid(row=4, column=3, columnspan=3, padx=3)

        if os.path.isfile("account.json"):
            if os.path.isfile("key.key"):
                account = RequestAccount()
                self.txtUser.insert(0, account['user'])
                self.txtPassword.insert(0, account['password'])

        #Check Saves
        self.checkboxs = Frame(self.container)
        self.checkboxs.pack(side=TOP, pady=5)

        self.varConn = BooleanVar()
        self.ckbConnection = Checkbutton(self.checkboxs, text="Save Connection", var=self.varConn, onvalue=True, offvalue=False)
        self.ckbConnection.grid(row=0, column=0)

        self.varAccount = BooleanVar()
        self.ckbAccount = Checkbutton(self.checkboxs, text="Save Account", var=self.varAccount, onvalue=True, offvalue=False)
        self.ckbAccount.grid(row=1, column=0)

        #Buttons
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
        conn = Conn(self.txtHost.get(), self.txtPort.get(), self.txtUser.get(), self.txtPassword.get())
        verify = conn.Open()

        if verify:
            self.session.Init(self.txtHost.get(), self.txtPort.get(), self.txtUser.get(), self.txtPassword.get())

            if self.varConn.get() or self.varAccount.get():
                verifySave1 = True
                verifySave2 = True

                if self.varConn.get():
                    verifySave1 = conn.SaveConn()

                if self.varAccount.get():
                    verifySave2 = conn.SaveAccount()

                if verifySave1 == False or verifySave2 == False:
                    messagebox.showerror(title="Error", message="Could not create save file")
                self.window.destroy()
            else:
                self.window.destroy()
        else:
            messagebox.showerror(title="Connection for SQL Server", message="Connection Refused")

    def Test(self, event):
        verify = Conn(self.txtHost.get(), self.txtPort.get(), self.txtUser.get(), self.txtPassword.get()).Test()

        if verify:
            messagebox.showinfo(title="Connection", message="Success!")
        else:
            messagebox.showerror(title="Connection Refused", message="Connection Refused")

    def Exit(self, event):
        self.window.destroy()

