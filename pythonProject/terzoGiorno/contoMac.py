class ContoMac:
    def __init__(self, numConto, credito):
        self.numConto = numConto
        self.credito = credito

    def ricarica(self, ricarica):
        self.credito += ricarica