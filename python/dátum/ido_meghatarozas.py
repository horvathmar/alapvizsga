import datetime

def current_time()-> list[int, int]:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    return [hour, minute]
current = current_time()




def beker(uzenet, min, max):
    valasz = int(input(f'{uzenet}: '))
    while valasz<min or valasz>max:
        print(f'{min} és {max} közötti értéket adjon meg.')
    return valasz

ora = beker("Kérem adja meg az órát: ", 0,23)
perc = beker("Kérem adja meg a percet: ", 0,59)
ido = ora * 60 + perc
aktualis_ido = current[0] * 60 + current[1]


if aktualis_ido > ido:
    print('A vizsgának már vége lett')
else:
    print(f'A vizsga hátralévő ideje: {ido - aktualis_ido} perc')