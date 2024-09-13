import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ilfoggia1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE PyDb")