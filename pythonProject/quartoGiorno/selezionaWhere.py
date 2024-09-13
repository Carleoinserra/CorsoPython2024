import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ilfoggia1",
  database="PyDb"
)

mycursor = mydb.cursor()
add = input("Inserisci l'indirizzo del cliente da cercare")
sql = "SELECT * FROM customers WHERE address = (%s)"
val = (add, )
mycursor.execute(sql, val)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)