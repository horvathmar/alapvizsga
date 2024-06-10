from random import randint

print('2. feladat: Halmaz-e?')
def generate():
    lista = []
    lista2 = []
    for i in range(8):
        lista.append(randint(1,9))
    for l in lista:
        if l not in lista2:
            print(f'{lista} Nem halmaz')
        else:
            print(f'{lista}Halmaz')


generate()