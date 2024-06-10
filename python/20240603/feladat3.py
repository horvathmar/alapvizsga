from toto import Totok

lista : list[Totok] = []

def main():
    file_open('toto.txt')
    print('3. feladat: Toto')
    print('3.1 feladat: Adatok beolvasása és tárolása')
    print(f'3.2 feladat: Fogadási fordulók száma: {len(lista)}')
    print(f'3.3 feladat: Telitalálatos szelvények száma: {telitalalat()} darab')
    if nem_volt_dontetlen() == True:
        print(f'3.4 feladat: Volt döntetlen mentes forduló!')
    else:
        print(f'3.4 feladat: Nem volt döntetlen mentes forduló!')


def file_open(filename: str):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        lista.append(Totok(row))
    file.close()

def telitalalat()->int:
    counter = 0
    for l in lista:
        counter += l.t13p1
    return counter

def nem_volt_dontetlen() ->bool:
    for l in lista:
        if 'X' not in l.eredmenyek:
            return True
    return False

main()
