lista = []


somma = 0
cont = 0
print("qualsiasi tasto per inserire una temperatura, e per uscrire : ")
scelta = input()
while scelta != 'e':
     temp = int(input("Scrivi una temperatura: "))
     cont += 1
     somma += temp
     lista.append(temp)
     print("qualsiasi tasto per inserire una temperatura, e per uscrire : ")
     scelta = input()

print(lista)
media = somma / cont
print("La media delle temperature è: ", media)

for x in lista:
     if x > media:
          print(x, " maggiore della media")
     elif x < media:
          print(x, " minore della media")
     else:
          print(x , " Uguale alla media")

