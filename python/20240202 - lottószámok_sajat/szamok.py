from szam import Szamok

szamok_listaja : list[Szamok] = []


def load_from_file(filename: str):
    file = open(filename, 'r', encoding='utf8')
    for row in file:
        szamok_listaja.append(Szamok(row.strip()))
    file.close()

def hozzaadas() -> int:
    print('1. feladat: az 52. hét számai')
    for i in range(1, 6):
        bekeres = int(input((f'{i}. szám: ')))
        szamok_listaja.append(bekeres)
        
# def szamok_rendezese():
#     print('1. feladat: az 52. hét számai')
#     for i in range(1, 6):
#         bekeres = int(input((f'{i}. szám: ')))
#     rendezett = sorted(bekeres)
#     print(rendezett)
        
# def bekeres():
#     het = int(input('Kérem a hetet: '))
#     if het == len(szamok_listaja):
#         print(len(het))