
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


# ------------------------------------------------
# 1 pytania
import time

biurko = Biurko()

while True:

    pytanie_poczatkowe = input('Dzien dobry, czy chcesz kupic biurko? wpisz tak/nie: ')
    if pytanie_poczatkowe == 'tak':
        print('super, oto konfigurator twojego biurka: ')
        print()
        biurko.dostepne_materialy()
        wybrany_material = input('wybierz dostępny materiał przepisujac jego nazwe: ')
      

        if wybrany_material in biurko.material:
            print(f'wybrałeś materiał: ',wybrany_material)

            biurko.dost_liczba_nog()
            wybrana_liczba_nog = int(input('Wybierz liczbe nog: '))

            if wybrana_liczba_nog in biurko.liczba_nog:
                print(5)

            else:
                print("wybierz poprawną liczbe nog: ")


#TUTAJ DZIAŁAM DALEJ



            break

        else:
            print('nie ma takiego materialu')
        time.sleep(3)

    elif pytanie_poczatkowe == 'nie':
        print('szkoda')
        break
    else:
        print('co ty wpisujesz?')
        time.sleep(3)
        continue
