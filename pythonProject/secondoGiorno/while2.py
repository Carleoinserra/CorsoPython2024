



'''num = 1
num1 = int(input("Scrivi il numero di cui vuoi la tabellina"))
while num <= 10:
    print(num * num1)
    num += 1'''
num1 = int(input("Scrivi un numero"))
cont = 0
somma = 0
while num1 != 0:
    num1 = int(input("Scrivi un numero"))
    somma += num1
    cont += 1

print("Hai iterato ", cont, " volte")
print("La somma dei numeri" , somma)