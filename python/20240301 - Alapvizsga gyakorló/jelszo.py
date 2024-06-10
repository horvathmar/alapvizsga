while True:
    felhasznalonev = input('Adja meg a felhasználónevét!')
    jelszo = input('Adja meg a jelszavát!')
    if felhasznalonev == 'bori99' and jelszo == 'Szivecske<3':
        print('Belépés engedélyezve')
        break
    else:
        print('Belépés megtagadva.')