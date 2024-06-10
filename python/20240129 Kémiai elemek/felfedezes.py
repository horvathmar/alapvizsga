from felfedezesek import Adatok

adatok_listaja : list[Adatok] = []

def load_from_file(filename: str) -> None:
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        adatok_listaja.append(Adatok(row.strip()))
    file.close()

def okori_felfedezesek():
    counter = 0
    for row in adatok_listaja:
        if row.ev == 'Ókor':
            counter += 1
    print(f'4. feladat: Felfedezések száma az ókorban: {counter}')

def bekeres() -> str:
    kereses = input('5. feladat: Kérek egy vegyjelet: ')
    for c in kereses:
        if (c < "A" or c > "z") or len(kereses) > 2:
            bekeres()
        else:
            print(kereses)
    return kereses

def kereso(kereses: str) -> Adatok|None:
    for e in adatok_listaja:
        if e.vegyjel.lower() == kereses.lower():
            return e
    return None
            
def leghosszabb_ido():
    hosszu_ido = 0
    for c in adatok_listaja:
        if c.ev == hosszu_ido and c.ev != 'Ókor':
            c.ev - c ==hosszu_ido
    print(hosszu_ido)