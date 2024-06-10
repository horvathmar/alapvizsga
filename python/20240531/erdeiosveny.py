from random import randint

def main():
    lista = []
    for i in range(25):
        lista.append(randint(0,1))
    print(lista)
    if atkeles(lista):
        print('Piroska át tud kelni a száraz lábbal az ösvényen.')
    else:
        print('Piroska nem tud kelni a száraz lábbal az ösvényen.')

def atkeles(lista: list[int]) -> bool:
    pocsolyak = 0
    for l in lista:
        if l == 1:
            pocsolyak += 1

            if pocsolyak == 4:
                return False
            return True
        else:
            pocsolyak = 0
        

main()