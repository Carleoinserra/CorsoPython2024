
num = 9
for x in range (1,11):
    print(x * num)

lista = [3, 4, 5, 6]
somma = 0
print("Elementi lista")
numPre = int(input("Cerca un numero"))
trovato = False
for i , p in enumerate(lista):
    print("Elemento indice : ", i)
    print(p)
    somma += p
    if p == numPre:
        trovato = True

print("La somma dei numeri è" , somma)

if trovato == True:
    print("Numero presente")
else:
    print("Numero non presente")