from kuldetes import Kuldetes

kuldetesek_listaja : list[Kuldetes] = []
def main():
    file_open('kuldetesek.csv')
    print('3. feladat')
    print(f'\tÖsszesen {len(kuldetesek_listaja)} alkalommal indítottak űrhajót.')
    print('4. feladat')
    print(f'\t{ossz_legenyseg()} indult az űrbe összesen.')
    print('5. feladat')
    print(f'\tÖsszesen {otnel_kevesebb()} alaklommal küldtek kevesebb, mint 5 embert az űrbe.')
    print('6. feladat')
    print(f'\t{nem_landolt()} asztronauta volt a Columbia fedélzetén annak utolsó útján')
    print('7. feladat')
    legtobb = legtobb_ido()
    print(f'\tA leghosszabb ideig a {legtobb.ursiklo_neve} volt az űrben a {legtobb.kod} kuldetes során.')
    print(f'\tÖsszesen {legtobb.ossz_ora} órát volt távol a Földtől')
    print('8. feladat')
    counter = szamlalo()
    if szamlalo != 0:
        print(f'\tEbben az évben {counter} küldetés volt.')
    else:
        print('\tEbben az évben nem indult küldetés')

    print('9. feladat')
    print(f'\tA küldetések {round(szazalek(), 2)}%-a fejeződött be a Kennedy űrközpontban.')
    write_to_file('ursiklok.txt')


def file_open(filename: str):
    file = open(filename, 'r', encoding='utf-8')
    for k in file:
        kuldetesek_listaja.append(Kuldetes(k))
    file.close()

def ossz_legenyseg():
    counter = 0
    for k in kuldetesek_listaja:
        counter += k.legenyseg
    return counter

def otnel_kevesebb():
    counter = 0
    for k in kuldetesek_listaja:
        if k.legenyseg < 5:
            counter += 1
    return counter

def nem_landolt():
    for k in kuldetesek_listaja:
        if k.legitamasz == 'nem landolt' and k.ursiklo_neve == 'Columbia':
            return k.legenyseg

def legtobb_ido():
    legtobb = kuldetesek_listaja[0]
    for k in kuldetesek_listaja:
        if k.ossz_ora == legtobb.ossz_ora:
            legtobb = k
    return legtobb

def szamlalo():
    counter = 0
    ev = int(input('\tÉvszám: '))
    for k in kuldetesek_listaja:
        if k.evszam == ev:
            counter += 1
    return counter

def szazalek():
    counter = 0
    osszeg = len(kuldetesek_listaja)
    for k in kuldetesek_listaja:
        if k.legitamasz == 'Kennedy':
            counter += 1
    return  counter / osszeg *100

def write_to_file(filename):
    file = open(filename, 'w', encoding='utf-8')
    for k in kuldetesek_listaja:
        file.write(f'{k.legitamasz}\t{k.ossz_ora}\n')
    file.close()




main()