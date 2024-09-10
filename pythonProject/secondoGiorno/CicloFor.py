for x in range(6):
    print(x)


# stampiamo la tabellina del 9
num = 9
for x in range(11):
    print(x * num)


# stampiamo i numeri dispari
for x in range(11):
    if (x % 2) != 0:
        print(x)






lista = ["Carlo", "Antonio", "maria"]

for i in lista:
    print(i)


# stampiamo sia l'indice che il valore dell'elemento
for indice, valore in enumerate(lista):
    print(f"Indice: {indice}, Valore: {valore}")