#példa egy dátum használatos feladatra

import datetime

def jelenlegi_ido()-> list[int, int]:
    ora = datetime.datetime.now().hour
    perc = datetime.datetime.now().minute
    return [ora, perc]
jelenlegi = jelenlegi_ido()




def beker(uzenet, min, max):
    valasz = int(input(f'{uzenet}: '))
    while valasz<min or valasz>max:
        print(f'{min} és {max} közötti értéket adjon meg.')
    return valasz

ora = beker("Kérem adja meg az órát: ", 0,23)
perc = beker("Kérem adja meg a percet: ", 0,59)
ido = ora * 60 + perc
aktualis_ido = jelenlegi[0] * 60 + jelenlegi[1]


if aktualis_ido > ido:
    print('A vizsgának már vége lett')
else:
    print(f'A vizsga hátralévő ideje: {ido - aktualis_ido} perc')