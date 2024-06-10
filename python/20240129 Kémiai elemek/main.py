from felfedezes import *

def main():
    load_from_file('felfedezesek.csv')
    print(f'3. feladat: Elemek száma: {len(adatok_listaja)}')
    okori_felfedezesek()
    bekeres()
    keresett_elem = kereso()
    if keresett_elem == None:
        print('Nincs ilyen elem az adatforrásban')
    else:
        print(f'Az elem vegyjele: {keresett_elem.vegyjel}')
        print(f'Az elem neve {keresett_elem.nev}')
        print(f'Rendszám: {keresett_elem.rendszam}')
        print(f'felfedezés éve: {keresett_elem.ev}')
        print(f'Felfedező: {keresett_elem.felfedezo}')
    leghosszabb_ido()
main()