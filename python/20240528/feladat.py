def number_input(szöveg, maximum):
    szam = 0
    while szam <= 0 or szam > maximum:
        try:
            szam = int(input(szöveg))
        except:
            print('Nem megfelelő szám!')
    return szam

def eltelt_napok_szama(ev, honap, nap, masodik_ev, masodik_honap, masodik_nap):
    atvaltva = ev * 365 + honap * 31 + nap
    atvaltva2 = masodik_ev * 365 + masodik_honap * 31 + masodik_nap
    return abs(atvaltva2 - atvaltva)


ev = number_input('Kérem az első dátum évét: ', 2024)
honap = number_input('Kérem az első dátum hónapját: ', 12)
nap = number_input('Kérem az első dátum napját: ', 31)
masodik_ev = number_input('Kérem az második dátum évét: ', 2024)
masodik_honap = number_input('Kérem az második dátum hónapját: ', 12)
masodik_nap = number_input('Kérem az második dátum napját: ', 31)
print(f'{ev}.{honap}.{nap} és {masodik_ev}.{masodik_honap}.{masodik_nap} között {eltelt_napok_szama(ev, honap, nap, masodik_ev, masodik_honap, masodik_nap)} nap volt!')