class AniBisecti:
    def __init__(self, ani):
        self.ani = ani

    def filtreaza(self):
        rezultat = []
        for an in self.ani:
            # Verificam daca anul este bisect
            if an % 400 == 0 or (an % 4 == 0 and an % 100 != 0):
                rezultat.append(an)
        return rezultat


ani = [2000, 2020, 2023, 2024, 2100]
obiect = AniBisecti(ani)
print(obiect.filtreaza())
