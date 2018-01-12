import macierz
import random
import time
import genetyczny
import os


def run(tab):
    start = time.clock()
    int = random.randint(0, 100)

    gen = genetyczny.Genetyczny(tab, 0.01, 1000)

    end = time.clock()
    total = end - start
    print("{0:02f}s".format(total))

def pressAnyKeyToContinue():
    input("Wciśnij dowolny klawisz aby kontynuować...")


spisTSP = "1 -> 'gr17'\n2 -> 'gr24'\n3 -> 'gr48'\n4 -> 'gr120'"
spisATSP = "1 -> 'br17'\n2 -> 'ftc33'\n3 -> 'ftv47'\n4 -> 'ftv70'"
flag = False
while (flag != True):
    chose = input("Dla jakich instancji chcesz rozwiązać problem \n1-> Symetrycznych\n2-> Asymetrycznych\n3 -> Wyjscie")
    if chose == '1':
        print("Wybierz:")
        insTSP = input(spisTSP)
        if insTSP == '1':
            tab = macierz.creatematrix_TSP('gr17.tsp', 15)
            run(tab)
            pressAnyKeyToContinue()
            os.system("cls")
        elif insTSP == '2':
            tab = macierz.creatematrix_TSP('gr24.tsp', 15)
            run(tab)
            pressAnyKeyToContinue()
            os.system("cls")
        elif insTSP == '3':
            tab = macierz.creatematrix_TSP('gr48.tsp', 15)
            run(tab)
            pressAnyKeyToContinue()
            os.system("cls")
        elif insTSP == '4':
            tab = macierz.creatematrix_TSP('gr120.tsp', 19)
            run(tab)
            pressAnyKeyToContinue()
            os.system("cls")
        else:
            print("Zły wybór")
            pressAnyKeyToContinue()
            os.system("cls")

    elif chose == '2':
        print("Wybierz:")
        insTSP = input(spisATSP)
        if insTSP == '1':
            tab = macierz.creatematrix_ATSP('br17.atsp', 16, '9999')
            run(tab)
            pressAnyKeyToContinue()
            os.system("cls")
        elif insTSP == '2':
            tab = macierz.creatematrix_ATSP('ftv33.atsp', 15, '100000000')
            run(tab)
            pressAnyKeyToContinue()
            os.system("cls")
        elif insTSP == '3':
            tab = macierz.creatematrix_ATSP('ftv47.atsp', 15, '100000000')
            run(tab)
            pressAnyKeyToContinue()
            os.system("cls")
        elif insTSP == '4':
            tab = macierz.creatematrix_ATSP('ftv70.atsp', 15, '100000000')
            run(tab)
            pressAnyKeyToContinue()
            os.system("cls")
        else:
            print("Zły wybór")
            pressAnyKeyToContinue()
            os.system("cls")
    elif chose == '3':
        flag = True
    else:
        print("Zły wybór")
        pressAnyKeyToContinue()
        os.system("cls")
