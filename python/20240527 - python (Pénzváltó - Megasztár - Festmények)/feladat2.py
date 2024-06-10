import random
lista = []
for i in range(5):
    lista.append(random.randint(1,10))


def osszpontszam(lista: list[int]) ->int:
    legnagyobb = lista[0]
    osszeg = 0
    for l in lista:
        if l > legnagyobb:
            legnagyobb = l
        osszeg += l
    return osszeg - legnagyobb

print(f'{lista} -> összpontszám: {osszpontszam(lista)} pont')