import pymssql

conn = pymssql.connect(server='den1.mssql8.gear.host',
                       user='invictusmaster',
                       password='Invictus@123',
                       port='1433',
                       database='invictusmaster')
cursor = conn.cursor()

#with open('contatos.json') as f:
#    contatos = json.load(contatos, f)
