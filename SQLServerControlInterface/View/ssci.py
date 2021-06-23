from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from View.openConn import *
from Model.connectDB import *

ConnectionReady = False

class SSCI:
    def __init__(self, master=None):
        self.master = master

        self.window = Frame(master)
        self.window.pack(side=TOP, fill="both")

        #Menu
        menubar = Menu(self.master)

        filemenu = Menu(menubar)
        filemenu.add_command(label="Connect", command=self.Connect)
        filemenu.add_command(label="Disconnect", command=self.Disconnect)
        filemenu.add_command(label="Exit SSCI", command=self.ExitSSCI)

        menubar.add_cascade(label="File", menu=filemenu)

        self.master.config(menu=menubar)

        #Options up
        self.up = Frame(self.window)
        self.up.pack(side=TOP, fill="both")

        self.btnRun = Button(self.up, text="RUN", bg="green", command=self.InsertTable)
        self.btnRun.grid(row=0, column=0, padx=2, pady=2)
        self.btnRun['state'] = DISABLED

        #Scrollbar/Query's
        self.querys = Frame(self.window)
        self.querys.pack(side=TOP, fill="both")

        self.cs = Scrollbar(self.querys, orient="vertical")
        self.cs.pack(side=RIGHT, fill="y")

        self.txtQuery = Text(self.querys, relief="raise", yscrollcommand=self.cs.set)
        self.txtQuery.pack(fill="both")

        self.cs.config(command=self.txtQuery.yview)

        #DataTable
        self.dataTable = Frame(self.window)
        self.dataTable.pack(side=BOTTOM, fill="both")

        #columns = ("#1", "#2")

        #self.table = ttk.Treeview(self.dataTable, columns=columns, show="headings")
        #self.table.heading("0", text="Teste", anchor=CENTER)
        #self.table.heading("1", text="Teste", anchor=CENTER)
        #self.table.insert(parent="", index=0, iid=0, text="", values=("1", "Vineet", "Alpha"))
        #self.table.insert(parent="", index=1, iid=1, text="", values=("2", "Anil", "Bravo"))
        #self.table.pack(side=BOTTOM, fill="both")

    #Open Connect
    def Connect(self):
        self.open = Toplevel()
        OpenConnect(self.open)
        self.open.protocol("WM_DELETE_WINDOW", self.Close_win)
        self.open.transient(self.master)
        self.open.focus_force()
        self.open.grab_set()
        print('teste')

    def Close_win(self):
        self.open.destroy()
        self.open = None

        if ConnectionReady:
            self.btnRun['state'] = NORMAL

    def Disconnect(self):
        cursor.execute("select name from sys.tables")
        row = cursor.fetchone()
        print(row)
        self.btnRun['state'] = NORMAL

    def ExitSSCI(self):
        self.master.destroy()

    #
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
        print('teste')

    def Teste(self):
        messagebox.showinfo(title="Teste", message="Testeeeeeee")

#ssci = Tk()
#Main(ssci)
#ssci.title("SQL Server Control Interface for Unix")
#ssci.geometry("300x250+250+250")
#ssci.attributes("-zoomed", True)
#ssci.mainloop()
