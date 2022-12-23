
class Biurko:
    material = ['drewno', 'szklo', 'plastik']
    liczba_nog = [3, 4, 5, 6, 8]
    kolor = ['bialy', 'czarny', 'czerwony', 'niebieski', 'zolty']
    dlugosc = 180
    szerokosc = 70

    def wymiary(self, dlugosc, szerokosc):
        print(f'Wymiary biurka: dlugosc= {dlugosc}cm, szerokosc= {szerokosc}cm')

    def zmien_kolor(self, nowy_kolor):
        self.kolor = nowy_kolor
        print(f'Kolor zostal zmieniony na kolor: {nowy_kolor}')

    def info_o_kolorze(self):
        print(f'aktualny kolor biurka to: {self.kolor}')

    def dostepne_materialy(self):
        print(f'dostepne materialy to: {self.material}')

    def dost_liczba_nog(self):
        print(f'Dostepna liczba nog to: {self.liczba_nog}')

    def wybierz_material(self):
        self.material = str(wybrany_material)
        print(f'aktualnie wybrany material biurka to:{wybrany_material}')

    def moje_materialy(self):
        return self.material

