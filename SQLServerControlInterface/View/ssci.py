from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from globalConfig import *
from View.openConn import *
from View.settings import *
from Model.connectDB import *
from Control.session import *

session = Session()

class SSCI:
    def __init__(self, master=None):
        self.master = master

        self.window = Frame(master)
        self.window.pack(side=TOP, fill="both")

        #Menu
        menubar = Menu(self.master, bg="#1C1C1C")

        filemenu = Menu(menubar)
        filemenu.add_command(label="Connect", command=self.Connect, font=fontDefault)
        filemenu.add_command(label="Disconnect", command=self.Disconnect, font=fontDefault)
        filemenu.add_command(label="Exit SSCI", command=self.ExitSSCI, font=fontDefault)

        settingsmenu = Menu(menubar)
        settingsmenu.add_command(label="Settings", command=self.Settings, font=fontDefault)

        menubar.add_cascade(label="File", menu=filemenu, foreground="white", font=fontDefault)
        menubar.add_cascade(label="Tools", menu=settingsmenu, foreground="white", font=fontDefault)

        self.master.config(menu=menubar)

        #Options up
        self.up = Frame(self.window, bg="#363636")
        self.up.pack(side=TOP, fill="both")

        self.btnRun = Button(self.up, text="RUN", bg="green", command=self.InsertTable, font=fontDefault)
        self.btnRun.grid(row=0, column=0, padx=2, pady=2)

        #Scrollbar/Query's
        self.querys = Frame(self.window)
        self.querys.pack(side=TOP, fill="both")

        self.cs = Scrollbar(self.querys, orient="vertical")
        self.cs.pack(side=RIGHT, fill="y")

        self.txtQuery = Text(self.querys, height=15, relief="raise", yscrollcommand=self.cs.set, bg="#4F4F4F", foreground="white", font=fontQuery)
        self.txtQuery.pack(fill="both")

        self.cs.config(command=self.txtQuery.yview)

        #DataTable
        self.dataTable = Frame(self.window)
        self.dataTable.pack(side=BOTTOM, fill="both")

    #Open Connect
    def Connect(self):
        self.open = Toplevel()
        OpenConnect(self.open, session=session)
        self.open.protocol("WM_DELETE_WINDOW", self.CloseOpenConn)
        self.open.transient(self.master)
        self.open.focus_force()
        self.open.grab_set()

    def CloseOpenConn(self):
        self.open.destroy()
        self.open = None

    #Session Over
    def Disconnect(self):
        session.Over()

    #Exit this SSCI
    def ExitSSCI(self):
        self.master.destroy()

    #Open Settings Page
    def Settings(self):
        self.config = Toplevel()
        Settings(self.config)
        self.config.protocol("WM_DELETE_WINDOW", self.CloseSettings)
        self.config.transient(self.master)
        self.config.focus_force()
        self.config.grab_set()

    def CloseSettings(self):
        self.config.destroy()
        self.config = None

    #Insert Query Data
    def InsertTable(self):
        columns = ("#1", "#2")

        self.table = ttk.Treeview(self.dataTable, columns=columns, show="headings")
        self.table.heading("0", text="Teste", anchor=CENTER)
        self.table.heading("1", text="Teste", anchor=CENTER)
        self.table.insert(parent="", index=0, iid=0, text="", values=("1", "Vineet", "Alpha"))
        self.table.insert(parent="", index=1, iid=1, text="", values=("2", "Anil", "Bravo"))
        self.table.pack(side=BOTTOM, fill="both")

    def Ready(self):
        #self.btnRun['state'] = NORMAL
        #print('teste')
        pass

#ssci = Tk()
#Main(ssci)
#ssci.title("SQL Server Control Interface for Unix")
#ssci.geometry("300x250+250+250")
#ssci.attributes("-zoomed", True)
#ssci.mainloop()
