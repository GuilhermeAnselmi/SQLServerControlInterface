import json

fontDefault = "arial 12"
fontQuery = "arial 15"

black = "black"

grey11 = "#1C1C1C"
grey21 = "#363636"
grey31 = "#4F4F4F"

silver = "#C0C0C0"
lightgrey = "#D3D3D3"
gainsboro = "#DCDCDC"
white = "white"

class Theme:
    def __init__(self):
        #bg
        self.background = None
        self.menu = None
        self.exec = None
        self.query = None

        #font
        self.fontMenu = None
        self.fontQuery = None

        try:
            with open("config.json") as f:
                theme = json.load(f)['theme']

            if theme == "Dark":
                self.Dark()
            elif theme == "Light":
                self.Light()
        except:
            self.Dark()

    def Dark(self):
        self.background = grey21
        self.menu = grey11
        self.exec = grey21
        self.query = grey31

        self.fontMenu = white
        self.fontQuery = white

    def Light(self):
        self.background = gainsboro
        self.menu = silver
        self.exec = lightgrey
        self.query = white

        self.fontMenu = black
        self.fontQuery = black

class Fonts:
    def __init__(self):
        #font
        self.default = fontDefault
        self.query = fontQuery
