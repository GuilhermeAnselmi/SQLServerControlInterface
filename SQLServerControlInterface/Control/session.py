import random

from Model.connectDB import *

class Session:
    def __init__(self):
        self.key = None
        self.active = False
        self.host = None
        self.port = None
        self.user = None
        self.password = None
        self.database = "master"

    def Init(self, host, port, user, password):
        seq = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = ""
        for i in range(10):
            key += random.choice(seq)

        self.key = key
        self.active = True
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def Over(self):
        self.key = None
        self.active = False
        self.host = None
        self.port = None
        self.user = None
        self.password = None
        self.database = "master"

    def SetDatabase(self, database):
        self.database = database
