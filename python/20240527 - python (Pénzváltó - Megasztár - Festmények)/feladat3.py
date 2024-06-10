from festmeny import Festmeny

lista : list[Festmeny] = []

def main():
    file_open('paintings.txt')
    print(f'3.3 feladat: A fájlban tárolt festmények száma: {len(lista)}')
    counter = picasso()
    print(f'3.4 feladat: A Pablo Picasso képek száma: {counter} darab.')
    legdragabb = draga()
    print(f'3.5 feladat: A legdrágább kép festője: {legdragabb.festo}, a kép címe: {legdragabb.nev}, becsült értéke: {legdragabb.ertek} dollár.')


def file_open(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        lista.append(row)
    file.close()

def picasso() ->int:
    counter = 0
    for l in lista:
        if l.festo == 'Pablo Picasso':
            counter += 1
    return counter

def draga():
    legdragabb = lista[0]
    for l in lista:
        if l > legdragabb:
            legdragabb = l
    return legdragabb

main()