from iranyito import Iranyitok

adatok_listaja : list[Iranyitok] = []

def main():
    file_open('NFL_iranyitok.txt')
    print(f'3. feladat: A statisztikában {len(adatok_listaja)} irányító szerepel')
    print('5. feladat: Legjobb irányítók: ')
    elerte()
    bekeres('legtobbeladott.txt')
    legtobb = legtobb_touchdown()
    print('7. feladat: A legtöbb TD-t szerző játékos: ')
    print(f'\tNeve: {legtobb.nev}')
    print(f'\tTD-k száma: {legtobb.td_passzok}')
    print(f'\tEladott labdák száma: {legtobb.eladott_labdak}')
    for key, value in statisztika().items():
        if value > 1:
            print(f'\t{key} - {value}')

def file_open(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        adatok_listaja.append(Iranyitok(row))        
    file.close()

def elerte():
    for i in adatok_listaja:
        if i.mutato_elso_szam > 100 and round(i.passzolt_yardok_meterre) > 4000:
            print(f'\t{i.nev} (Irányító mutató: {i.iranyito_mutato}, passzok: {i.passzolt_yardok_meterre} m.)')
    
def bekeres(filename):
    szam = int(input('6. feladat: Eladott labdák száma: '))
    file = open(filename, 'w', encoding='utf-8')
    for i in adatok_listaja:
        if szam < i.eladott_labdak:
            file.write(f'{i.nev}\n')
    file.close()

def legtobb_touchdown():
    legtobb = adatok_listaja[0]
    for i in adatok_listaja:
        if i.td_passzok > legtobb.td_passzok:
            legtobb = i
    return legtobb

def statisztika():
    egyetemek = {}

    for iranyito in adatok_listaja:
        if iranyito.egyetem in egyetemek:
            egyetemek[iranyito.egyetem] += 1
        
        else:
            egyetemek[iranyito.egyetem] = 1
    return egyetemek

            



main()