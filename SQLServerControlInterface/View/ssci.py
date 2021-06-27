from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from globalStyle import *
from View.openConn import *
from View.settings import *
from Model.connectDB import *
from Control.session import *

session = Session()
fonts = Fonts()

class SSCI:
    def __init__(self, master=None, theme=None):
        self.master = master

        self.window = Frame(master)
        self.window.pack(side=TOP, fill="both")

        #Menu
        menubar = Menu(self.master, bg=theme.menu)

        filemenu = Menu(menubar)
        filemenu.add_command(label="Connect", command=self.Connect, font=fonts.default)
        filemenu.add_command(label="Disconnect", command=self.Disconnect, font=fonts.default)
        filemenu.add_command(label="Exit SSCI", command=self.ExitSSCI, font=fonts.default)

        settingsmenu = Menu(menubar)
        settingsmenu.add_command(label="Settings", command=self.Settings, font=fonts.default)

        menubar.add_cascade(label="File", menu=filemenu, foreground=theme.fontMenu, font=fonts.default)
        menubar.add_cascade(label="Tools", menu=settingsmenu, foreground=theme.fontMenu, font=fonts.default)

        self.master.config(menu=menubar)

        #Exec's
        self.up = Frame(self.window, bg=theme.exec)
        self.up.pack(side=TOP, fill="both")

        self.btnRun = Button(self.up, text="RUN", bg="green", font=fonts.default, command=self.Run)
        self.btnRun.grid(row=0, column=0, padx=2, pady=2)

        #Scrollbar/Query's
        self.querys = Frame(self.window)
        self.querys.pack(side=TOP, fill="both")

        self.cs = Scrollbar(self.querys, orient="vertical")
        self.cs.pack(side=RIGHT, fill="y")

        self.txtQuery = Text(self.querys, height=15, relief="raise", yscrollcommand=self.cs.set, bg=theme.query, foreground=theme.fontQuery, font=fonts.query)
        self.txtQuery.bind("<Key>", self.Keypress)
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

    #Run this query
    def Run(self):
        if session.active:
            if self.txtQuery.get("1.0", END).strip() != "":
                verify = True
                use = False

                try:
                    #query = self.txtQuery.selection_get()      ERROR IN TRY EXCEPT
                    query = self.txtQuery.get("sel.first", "sel.last")
                except:
                    query = self.txtQuery.get("1.0", END)

                if query.split()[0].lower() == "use":
                    verify = Data(session=session).TestDatabase(query.split()[1].lower())

                    if verify:
                        session.SetDatabase(query.split()[1].lower())

                        if len(query.split()) <= 2:
                            use = True
                            messagebox.showinfo(title="Query Exec", message="Success sending query")
                        else:
                            query = " ".join(query.split()[2:])

                if verify and not use:
                    data = Data(session=session).Send(query)

                    if not data:
                        messagebox.showwarning(title="Incorrect Query", message="This query has incorrect instructions and/or arguments that do not exist in the database.")
                    else:
                        try:
                            execute = True

                            while execute:
                                row = data.fetchall()

                                if len(row) != 0:
                                    for line in row:
                                        print(line)

                                    print("Next table")
                                else:
                                    execute = False
                        except:
                            messagebox.showwarning(title="Incorrect Query", message="This query has incorrect instructions and/or arguments that do not exist in the database.")
                elif not verify:
                    messagebox.showwarning(title="Database does not exists", message="The database entered was not found")
        else:
            messagebox.showwarning(title="Server Not Connected", message="No connection to servers found")

    def Keypress(self, event):
        if event.keycode == 71:
            self.Run()

    #Insert Query Data
    def InsertTable(self):
        columns = ("#1", "#2")

        self.table = ttk.Treeview(self.dataTable, columns=columns, show="headings")
        self.table.heading("0", text="Teste", anchor=CENTER)
        self.table.heading("1", text="Teste", anchor=CENTER)
        self.table.insert(parent="", index=0, iid=0, text="", values=("1", "Vineet", "Alpha"))
        self.table.insert(parent="", index=1, iid=1, text="", values=("2", "Anil", "Bravo"))
        self.table.pack(side=BOTTOM, fill="both")

#ssci = Tk()
#Main(ssci)
#ssci.title("SQL Server Control Interface for Unix")
#ssci.geometry("300x250+250+250")
#ssci.attributes("-zoomed", True)
#ssci.mainloop()
