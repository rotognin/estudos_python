import datetime
import mysql.connector
import cliente

def dataAtual():
    data = datetime.datetime.now()
    return str(data.strftime('%d/%m/%Y %H:%M:%S'))


print('*** Rodrigo Tognin ***')
print(dataAtual())

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'python_db'
)

#print (mydb)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM clientes_tb WHERE cli_id = 1')
myresult = mycursor.fetchall()

print(myresult)
if (len(myresult) == 0):
    print ('Não existem clientes a serem exibidos')
    exit()

cliente = cliente.Cliente(myresult[0])
cliente.exibir()