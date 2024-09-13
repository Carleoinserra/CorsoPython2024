import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ilfoggia1",
  database="PyDb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"


val = ("Antonio", "Via Bologna 65")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")