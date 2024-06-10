valasz = input('Eurót (EUR) vagy forintot (HUF) akarsz váltani?')
if valasz == 'EUR':
    valasz2 = int(input('Hány eurót akarsz beváltani?'))
    print(f'{valasz2} euróért {valasz2*365} forintot kapsz.')
else:
    valasz3 = int(input('Hány forintot akarsz beváltani?'))
    print(f'{valasz3} forintért {round(valasz3/365, 2)} eurót kapsz.')

