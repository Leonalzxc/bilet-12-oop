class SumaCifrelor:
    def __init__(self, numere):
        self.numere = numere

    def calculeaza(self):
        rezultat = []
        for numar in self.numere:
            suma = 0
            # Parcurgem fiecare cifra a numarului
            for cifra in str(abs(numar)):
                suma = suma + int(cifra)
            rezultat.append(suma)
        return rezultat


numere = [123, 45, 678, 90]
obiect = SumaCifrelor(numere)
print(obiect.calculeaza())
