from View.ssci import *

class Main:
    interface = Tk()
    SSCI(interface)
    interface.title("SQL Server Control Interface for Unix")
    #interface.geometry("300x250+250+250")
    interface.attributes("-zoomed", True)
    interface.configure(bg="#363636")
    interface.mainloop()
