import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="gautham", passwd="1234", database="hacknjit")

mycursor = mydb.cursor()

mycursor.execute("select * from wallets")

for i in mycursor:
    print(i)