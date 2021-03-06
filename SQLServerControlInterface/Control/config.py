import json

class Config:
    def __init__(self):
        self.theme = None
    
    def CreateDefaults(self):
        try:
            configs = {
                "theme": "Dark"
            }

            with open("config.json", "w") as f:
                json.dump(configs, f)
        except ValueError:
            print(ValueError)

    def Save(self, theme):
        try:
            configs = {
                "theme": theme
            }

            with open("config.json", "w") as f:
                json.dump(configs, f)

            return True
        except:
            return False
