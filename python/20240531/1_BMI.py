from math import sqrt
tomeg = float(input('Kérem a test tömeget (kg): '))
magassag = float(input('Kérem a magasságot (m): '))
testtomeg_index = tomeg / (magassag * magassag)
kerekitett = round(testtomeg_index, 2)
print(f'A testtömeg indexed: {testtomeg_index}')
if kerekitett > 20 and kerekitett < 25:
    print('Normális a testalkatod!')
elif kerekitett < 20:
    print('Sovány vagy.')
else:
    print('Túlsúlyos vagy.')