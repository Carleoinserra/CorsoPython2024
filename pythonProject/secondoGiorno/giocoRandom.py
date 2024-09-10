import random
number = random.randint(1, 30)


vite = 5
vinto = False
while vite > 0:
    num =  int(input("Indovina il numero"))
    if num == number:

        vite = 0
        vinto = True
    else:
        if num > number:
            print("Il numero che hai inserito è maggiore")
            vite -= 1
        elif num < number:
            print("Il numero che hai inserito è minore")
            vite -= 1

if vinto:
    print("Hai vinto il gioco")
else:
    print("Game over")
    print("Il numero da infovinare era ", number)
