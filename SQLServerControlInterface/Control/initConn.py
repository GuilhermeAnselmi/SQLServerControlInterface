import pymssql
import json
import os.path

from cryptography.fernet import Fernet

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

    def SaveConn(self):
        try:
            connection = {
                "host": self.host,
                "port": self.port
            }

            with open("connection.json", "w") as f:
                json.dump(connection, f)

            return True
        except:
            return False

    def SaveAccount(self):
        key = Fernet.generate_key()
        suite = Fernet(key)

        archive = open("key.key", "w")
        archive.write(key.decode())

        user = suite.encrypt(self.user.encode())
        password = suite.encrypt(self.password.encode())

        try:
            account = {
                "user": user.decode(),
                "password": password.decode()
            }

            with open("account.json", "w") as f:
                json.dump(account, f)

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

def RequestConn():
    with open('connection.json') as f:
        return json.load(f)

def RequestAccount():
    with open('account.json') as f:
        account = json.load(f)

    key = open('key.key', 'r')
    key = key.readline().encode()
    suite = Fernet(key)
    user = suite.decrypt(account['user'].encode())
    password = suite.decrypt(account['password'].encode())

    account = {
        "user": user,
        "password": password
    }

    return account
