import json

fontDefault = "arial 12"
fontQuery = "arial 15"

grey11 = "#1C1C1C"
grey21 = "#363636"
grey31 = "#4F4F4F"

class Theme:
    def __init__(self):
        #bg
        self.background = None
        self.menu = None
        self.exec = None

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

    def Light(self):
        self.background = grey21
        self.menu = grey11
        self.exec = grey21

class Fonts:
    def __init__(self):
        #font
        self.default = fontDefault
        self.query = fontQuery
