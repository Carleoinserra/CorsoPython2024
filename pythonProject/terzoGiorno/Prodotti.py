class prodotti:
    def __init__(self, nome, articoli):
        self.nome = nome
        self.articoli = articoli


    def __str__(self):
        return f"{self.nome}, {self.articoli}"