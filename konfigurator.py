# 1 pytania
import time
from biurko import Biurko

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
