import math
def main():
    for i in range(3):
        film_cime = input('Add meg egy film címét! ')
        hossz = int(input('Hány perces a film? '))
        print(f'A(z) {film_cime} című film {atvaltas(hossz)} hosszú')

def atvaltas(hossz: int) ->str:
    ora = math.floor(hossz / 60)
    perc = hossz - ora * 60
    return str(ora) + ' óra ' + str(perc) + ' perc '

main()