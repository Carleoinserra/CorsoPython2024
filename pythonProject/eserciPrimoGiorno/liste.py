
listaStringhe = ["Carlo", "Antonio", "Maria", "Giulia"]

print(listaStringhe)

# accesso agli elementi della lista
print(listaStringhe[3])

# chiamo il metodo append per aggiungere un elemento alla lista
listaStringhe.append("Osvaldo")
print(listaStringhe)

# insert aggiunge un elemento nella posizione specificata
listaStringhe.insert(0, "AnnaMaria")
print(listaStringhe)

# len ritorna la lugnhezza della lista
print(len(listaStringhe))

# pop elimina un elmento in posizione
listaStringhe.pop(2)
print(listaStringhe)

# remove elimina un elmento a partire sal suo valore
listaStringhe.remove("Giulia")
print(listaStringhe)

lista1 = []

lista1.append(listaStringhe[0])
lista1.append(listaStringhe[1])
lista1.append(listaStringhe[2])

print(lista1)


