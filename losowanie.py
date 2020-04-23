import random

tab = []


def czy_byla_wylosowana(tablica, rozmiar, liczba_wylosowana):
    if rozmiar > 0:
        for i in range(rozmiar):
            if tablica[i] == liczba_wylosowana:
                return True
        return False


def losowa_liczba():
    return random.randint(1,10)

def main():
    rozmiar = 10
    liczba_wylosowanych = 0
    while liczba_wylosowanych < rozmiar:
        wylosowana = losowa_liczba()
        if not czy_byla_wylosowana(tab, liczba_wylosowanych, wylosowana):
            liczba_wylosowanych += 1
            tab.append(wylosowana)


    for i in range(rozmiar):
        print(tab[i])

main()
