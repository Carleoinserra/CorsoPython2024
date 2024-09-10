parola = input("Scrivi una parola: ")
parola1 = input("Scrivi una parola: ")

if parola == parola1:
    print("Sono uguali")
elif parola.lower() == parola1.lower():
    print("Sono quasi uguali")
else:
    print("Sono diverse")