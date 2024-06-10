from kuldetes import Kuldetesek

adatok_listaja : list[Kuldetesek] = []

def main():
    file_open('kuldetesek.csv')
    print('3. feladat')
    print(f'\tÖsszesen {len(adatok_listaja)} alkalommal indítottak űrhajót.')
    print('4. feladat')
    print(f'\t{utast_szallitot()} utas indult az űrbe összesen.')
    print('5. feladat')
    print(f'\tÖsszesen {alkalom_szama()} alkalommal küldtek kevesebb, mint 5 embert az űrbe.')
    print('6. feladat')
    print(f'\t{columbia_legenyseg_szama()} asztronauta volt a Columbia fedélzetén annak utolsó útján')
    print('7. feladat')
    leghosszabb = leghosszabb_ido()
    print(f'\tA leghosszabb ideig a {leghosszabb.nev} volt az űrben a {leghosszabb.kod} küldetés során.')
    print(f'\tÖsszesen {leghosszabb.ossz_ora} órát volt távol a Földtől')
    print('8. feladat')
    print(f'\tEbben az évben {ev_kereses()} küldetés volt.')
    print('9. feladat')
    print(f'\tA küldetések {kenedy_szama():0.2f}-a fejeződött be az Kennedy űrközpontban.')
    statistika_fajlba('ursiklo.txt')


def file_open(filename: str):
    file = open(filename, 'r', encoding='utf-8')
    for row in file:
        adatok_listaja.append(Kuldetesek(row))
    file.close()


def utast_szallitot():
    counter = 0
    for k in adatok_listaja:
        counter += k.legenyseg_szama
    return counter

def alkalom_szama():
    counter = 0
    for k in adatok_listaja:
        if k.legenyseg_szama < 5:
            counter += 1
    return counter

def columbia_legenyseg_szama():
    for k in adatok_listaja:
        if k.tamaszpont_neve == 'nem landolt' and k.nev == 'Columbia':
            return k.legenyseg_szama
        
def leghosszabb_ido():
    leghosszabb = adatok_listaja[0]
    for k in adatok_listaja:
        if k.ossz_ora == leghosszabb.ossz_ora:
            leghosszabb = k
    return leghosszabb



def ev_kereses():
    counter = 0
    evszam = int(input('\tÉvszám: '))
    for k in adatok_listaja:
        if k.ev == evszam:
            counter += 1
    return counter

def kenedy_szama():
    counter = 0
    for k in adatok_listaja:
        if k.tamaszpont_neve == 'Kennedy':
            counter += 1
    return counter / len(adatok_listaja) *100
        

def statistika_fajlba(filename):
    stat = {}
    for k in adatok_listaja:
        if k.nev not in stat.keys():
            stat[k.nev] = k.ossz_ora
        else:
            stat[k.nev] += k.ossz_ora
    
    file = open(filename, 'w', encoding='utf-8')
    for key, value in stat.items():
        file.write(f'{key}\t{round(value / 24, 2)}\n')
    file.close()


main()