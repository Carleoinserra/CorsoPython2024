listaD = {"nome": ["Carlo", "Antonio"], "mansioni": ["Operaio","funzionario"] }


print(listaD["nome"][0])
print(listaD["mansioni"][0])

for i, p in zip(listaD["nome"], listaD["mansioni"]):
    print(f"Nome: {i}, Mansione: {p}")
