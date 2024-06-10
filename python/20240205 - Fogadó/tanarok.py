from tanar import Tanarok

adatok_listaja : list[Tanarok] = []

def file_open(filename: str):
    file = open(filename, 'r', encoding='utf8')
    for row in file:
        adatok_listaja.append(Tanarok(row))
    file.close()

def tanar_idopontfoglalasanak_szama():
    tanar_neve = input('Adjon meg egy nevet: ')
    counter = 0
    for t in adatok_listaja:
        if tanar_neve == t.nev:
            counter += 1
    if counter == 0:
        print('A megadott néven nincs időpontfoglalás.')
    elif counter != 0:
        print(f'{tanar_neve} néven {counter} időpontfoglalás van.')
        
       
        
def idopont_bekeres():
    adott_idok_listaja : list[str] = []
    idopont = input('Adjon meg egy érvényes időpontot (pl. 17:10): ')
    for t in adatok_listaja:
        if idopont == t.idopont:
            adott_idok_listaja.append(t.nev)
    # return print(t.nev)
    filename = idopont.replace(':', '') + '.txt'
    adott_idok_listaja.sort()
    file = open(filename, 'w', encoding='utf8')
    for t in adott_idok_listaja:
        print(t)
        file.write(f'{t}\n')
    file.close

def legkorabban_lefoglalt(legkorabbi_idopont):
    legkorabbi_idopont = adatok_listaja[0]
    for t in adatok_listaja:
        if t.foglalas_ideje < legkorabbi_idopont.foglalas_ideje:
            t = legkorabbi_idopont
    return print(legkorabbi_idopont)

