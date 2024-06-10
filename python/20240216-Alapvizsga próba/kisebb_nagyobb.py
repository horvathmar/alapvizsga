print('1. feladat: Kisebb-nagyobb meghatározás')
elso_szam = int(input('Kérem az első számot: '))
masodik_szam = int(input('Kérem a második számot: '))
if elso_szam > masodik_szam:
    print(f'A nagyobb szám {elso_szam}, a kisebb {masodik_szam}')
elif masodik_szam > elso_szam:
    print(f'A nagyobb szám {masodik_szam}, a kisebb {elso_szam}')
else:
    print('A két szám egyenlő')