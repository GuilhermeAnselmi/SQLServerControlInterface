from View.ssci import *
from globalStyle import *

import os

theme = Theme()

class Main:
    # Check if the file exists
    if not os.path.isfile("config.json"):
        Config().CreateDefaults()

    interface = Tk()
    SSCI(interface, theme=theme)
    interface.title("SQL Server Control Interface for Unix")
    #interface.geometry("300x250+250+250")
    interface.attributes("-zoomed", True)
    interface.configure(bg=theme.background)
    interface.mainloop()
