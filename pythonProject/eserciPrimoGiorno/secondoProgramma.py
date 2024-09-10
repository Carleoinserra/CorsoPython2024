'''anni = int(input("Scivi la tua età: "))

anniAdd = anni + 10
print(f"Tra dieci anni avrai {anni+10}")'''

# con le fstring possiamo decidere quanti numeri decimali stampare di un numero float
num_dec = 3.23456

print(f"{num_dec:.2f}")

lista = ["carlo", "antonio", "lucia"]


# append aggiunge un elemento alla lista

lista.append("mario")
print(lista)

#copy: copia il contenuto di una lista in un’altra lista

lista1 = lista.copy()
print(lista1)

#count: conta il numero di occorrenze di un determinato valore in una lista
print(lista.count("carlo"))

#insert: inserisce un elemento prima della posizione specificata come primo argomento

lista.insert(0, "maria")
print(lista)

print(len(lista))

#pop: estrae dalla lista (e rimuove dalla lista) l’elemento nella posizione specificata;

lista.pop(2)
print(lista)

#remove: rimuove dalla lista la prima occorrenza del valore specificato come argomento;

lista.remove("maria")
print(lista)


'''num = int(input("scrivi un numero:"))

if num % 2 == 0:
    print(f"{num} è un numero pari")
else:
    print(f"{num} è un numero dispari")'''


#istruzione elif e confronto tra stringhe
'''
stringa = input("Scrivi una parola: ")
stringa1 = input("Scrivi un'altra parola: ")

if stringa == stringa1:
    print("Le due stringhe sono uguali")
elif stringa.lower() == stringa1.lower():
    print("le due stringhe sono quasi uguali")
else:
    print("Le due stringhe sono diverse")
'''

# operatori logici

username = "rossi"
password = "1234"

user = input("Scrivi lo user: ")
pswd = input("Scrivi la password")

if (user == username and password == pswd):
    print("Accesso consentito")
elif(user == username and password != pswd):
    print("Password non ricnosciuta")
elif(user != username and password == pswd):
    print("Username non riconosciuto")
else:
    print("Accesso non consentito")


