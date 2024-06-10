from tanarok import *

def main():
    file_open('fogado.txt')
    print('2. feladat')
    print(f'Foglalások száma: {len(adatok_listaja)}')
    print('3. feladat')
    tanar_idopontfoglalasanak_szama()
    print('4. feladat')
    idopont_bekeres()
    # print('5.feladat')
    # legkorabbi_idopont = legkorabban_lefoglalt()
    # print(f'Tanár neve: {legkorabbi_idopont.nev}')
    # print(f'Foglalt időpont: {legkorabbi_idopont.foglalt_idopont}')
    # print(f'Foglalás ideje: {legkorabbi.foglalas_idopontja}')
main()