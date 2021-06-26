import pymssql

#conn = pymssql.connect(server='',user='',password='',port='',database='')
#cursor = conn.cursor()

class Data:
    def __init__(self, session):
        self.conn = pymssql.connect(server=session.host, port=session.port, user=session.user, password=session.password,
                                    database=session.database)
        self.cursor = self.conn.cursor()

    def Send(self, query):
        try:
            exec = self.cursor.execute(query)
        except:
            return 0

        try:
            row = self.cursor.fetchone()
            return row
        except:
            return 1

    def TestDatabase(self, database):
        try:
            exec = self.cursor.execute("use " + database)
            self.conn.close()
            return True
        except:
            return False
