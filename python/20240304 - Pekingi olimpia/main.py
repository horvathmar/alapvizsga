from torna import Torna

resztvevok : list[Torna] = []
def main():
    file_open('torna.csv')
    print('2. feladat')
    print(f'Összesen {len(resztvevok)} versenyző indult a versenyen.')
    print()
    print('3. feladat')
    nyertes = korlat_nyertese()
    print(f'Korláton {nyertes.nev} szerezte meg az aranyérmet.')
    print()
    print('4. feladat')
    bekeres()
    print()
    print('5. feladat')
    nem_erte_el()
    print()
    print('6. feladat')
    foldeszek()
    print()
    print('7. feladat')
    for key, value in statisztika().items():
        print(f'{value} - {key}')


def file_open(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for r in file:
        resztvevok.append(Torna(r))
    file.close()

def korlat_nyertese():
    nyertes = resztvevok[0]
    for r in resztvevok:
        if r.korlat > nyertes.korlat:
            nyertes = r
    return nyertes

def bekeres():
    szam = int(input('Kérem a versenyző rajtszámát: '))
    for r in resztvevok:
        if szam == r.rajtszam:
            print(f'A {r.rajtszam} versenyző gyűrűn elért eredménye: {r.gyuru} pont.')
            break
    else:
        print('Nincs ilyen versenyző!')

def nem_erte_el():
    for r in resztvevok:
        if r.lolenges < 14.5:
            print(f'{r.nev}')

def foldeszek():
    foldeszek_listaja = []
    for r in resztvevok:
        if r.foldresz not in foldeszek_listaja:
            foldeszek_listaja.append(r.foldresz)
    for f in foldeszek_listaja:
        print(f, end=' ')
    
def statisztika() ->dict:
    stat = {}
    for r in stat:
        if r.kod in stat:
            stat[r.kod] += 1
        if r not in stat:
            stat[r.kod] = 1
    return stat
    


main()