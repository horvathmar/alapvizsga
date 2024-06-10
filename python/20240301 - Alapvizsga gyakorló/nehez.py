from allat import Allatfaj
allatok_listaja : list[Allatfaj] = []
def main():
    for i in range(3):
        fajnev = input('Adja meg a egy állatfaj nevét! ')
        tomeg = int(input('Hány kilogramm a tömege egy példánynak?'))
        allatok_listaja.append(Allatfaj(fajnev, tomeg))
    for i in range(3):
        print(f'A(z) {fajnev} tömege {tomeg} kg.')

    legnehez = legnehezebb()
    print(f'A legnehezebb állat a(z) {legnehez.fajnev}, tömege {legnehez.tomeg} kg.')
    write_to_file('legnehezebb.txt')


def legnehezebb():
    legnehezebb = allatok_listaja[0]
    for a in allatok_listaja:
        if a.tomeg > legnehezebb.tomeg:
            legnehezebb = a
    return legnehezebb

def write_to_file(filename: str):
    file = open(filename, 'w', encoding='utf-8')
    file.write(f'{legnehezebb().fajnev}')
    file.close()

main()    