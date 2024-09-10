import os
import pickle
import matplotlib.pyplot as plt
import numpy as np


class dipendente:
    def __init__(self, nome, mansione, stipendio):
        self.nome = nome
        self.mansione = mansione
        self.stipendio = stipendio

    def __str__(self):
        return f'Nome: {self.nome}, Mansione: {self.mansione}, stipendio: {self.stipendio}'

    def bonus(self):
        self.stipendio += 200



if os.path.exists("listaDipendenti.pkl"):
    with open("listaDipendenti.pkl", 'rb') as f:

        listaD = pickle.load(f)
else:
    d1 = dipendente("Rossi", "operaio", 1200)

    d1.bonus()

    d2 = dipendente("Bianchi", "funzionario", 2000)

    listaD = [d1, d2]



scelta = "1"
while scelta != "0":

    scelta = input("1 per inserire un nuovo dipendente 2 per stampare 0 per uscire")
    if scelta == "1":
        nome = input("Nome da dipendente: ")
        mansione = input("Mansione: ")
        stipendio = input("Stipendio: ")
        d3 = dipendente(nome, mansione, stipendio)
        listaD.append(d3)
    if scelta == "2":
        for dip in listaD:
            print(dip)
    if scelta == "3":
        nomeD = input("Nome dipendente: ")
        for dip in listaD:
            if dip.nome == nomeD:
                dip.bonus()

f = open("listaDipendenti.pkl", "wb")
pickle.dump(listaD, f)
f.close()
# Estrai i dati
nomi = [dipendente.nome for dipendente in listaD]
stipendi = [int(dipendente.stipendio) for dipendente in listaD]
# Grafico
plt.bar(nomi, stipendi)
plt.xlabel('Nomi Dipendenti')
plt.ylabel('Stipendi')
plt.title('Stipendi dei Dipendenti')
plt.show()




