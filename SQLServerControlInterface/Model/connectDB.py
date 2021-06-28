import pymssql

#conn = pymssql.connect(server='',user='',password='',port='',database='')
#cursor = conn.cursor()

class Data:
    def __init__(self, session):
        self.conn = pymssql.connect(server=session.host, port=session.port, user=session.user, password=session.password,
                                    database=session.database, autocommit=True)
        self.cursor = self.conn.cursor()

    def Send(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor
        except:
            return False

        #try:
            #self.cursor.fetchone()
            #return self.cursor
        #except:
            #return 1

    def TestDatabase(self, database):
        try:
            exec = self.cursor.execute("use " + database)
            self.conn.close()
            return True
        except:
            return False
