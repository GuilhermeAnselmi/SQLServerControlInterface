import pymssql
import json

class Conn:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def Open(self):
        try:
            conn = pymssql.connect(server=self.host,
                                   user=self.user,
                                   password=self.password,
                                   port=self.port,
                                   database='master')

            return True
        except:
            return False

    def Save(self):
        try:
            connection = {
                "host": self.host,
                "port": self.port,
                "user": self.user,
                "password": self.password
            }

            with open("connections.json", "w") as f:
                json.dump(connection, f)

            return True
        except:
            return False

    def Test(self):
        try:
            conn = pymssql.connect(server=self.host,
                                   user=self.user,
                                   password=self.password,
                                   port=self.port,
                                   database='master')

            return True
        except:
            return False
