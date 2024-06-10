def szokoev(ev) ->bool:
    if ev % 400 == 0:
        return True
    elif ev % 4 == 0 and ev % 100 != 0:
        return True
    return False

print('2. feladat: Szökőév listázó')
szam1 = int(input('Kérem az egyik számot: '))
szam2 = int(input('Kérem az másik számot: '))
if szam1 > szam2:
    szam1, szam2 = szam2, szam1
szokoevek = []
for i in range(szam1, szam2+1):
    if szokoev(i):
        szokoevek.append(i)
    
if len(szokoevek) == 0:
    print('Nincs szökőév a megadott tartományban')
else:
    print('Szökőévek:', end=' ')
    print(szokoevek)