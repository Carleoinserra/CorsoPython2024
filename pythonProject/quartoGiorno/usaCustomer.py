import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ilfoggia1",
  database="PyDb"
)


scelta = "2"

while scelta != "0":
    scelta = input("Premi 1 per inserire un nuovo cliente Premi 2 per cercare un cliente, 3 per rimuovere un cliente, 4 per vedere tutti i clienti")
    if scelta == "1":
            nome = input("Inserisci un nome: ")
            indirizzo = input("Inserisci un indirizzo: ")
            mycursor = mydb.cursor()

            sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
            val = (nome, indirizzo)
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")

    if scelta == "2":
        nome = input("Inserisci un nome: ")
        mycursor = mydb.cursor()

        sql = "SELECT * FROM customers WHERE name =  (%s)"
        # nela val dobbiamo inserire una virgola dopo il valore
        val = (nome,)
        mycursor.execute(sql, val)

        myresult = mycursor.fetchall()
        if len(myresult) > 0:
         for x in myresult:
            print(x)
        else:
            print("Nessun cliente")

    if scelta == "3":
        nome = input("Inserisci un nome: ")
        mycursor = mydb.cursor()

        sql = "DELETE FROM customers WHERE name =  (%s)"
        val = (nome,)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted")
    if scelta == "4":
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM customers")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

