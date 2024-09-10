import os
import pickle

class dipendente:
    def __init__(self, nome, mansione, stipendio):
        self.nome = nome
        self.mansione = mansione
        self.stipendio = stipendio
    def __str__(self):
        return f'{self.nome} {self.mansione} {self.stipendio}'

    def bonus(self):
        self.stipendio += 200
'''
d1 = dipendente("Rossi", "operaio", 1200)

print(d1)

d1.bonus()

print(d1)

lista = []

lista.append(d1)
f = open("testDipedente.pkl", "wb")
pickle.dump(lista, f)
f.close()
'''
# Caricamento della lista dei conti se esiste, altrimenti usa una lista vuota








