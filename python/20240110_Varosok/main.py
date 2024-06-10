from cities import *

def main():
    if not load_from_file('varosok.csv'):
        print('Sikertelen fájlművelet')
    else:
        print(f'A listában {len(cities)} város szerepel.')
        print(f'Legalább 10 milliós városok száma: {count_cities_over(10000000)}.')
        print('Legnépesebb város: ')
        highest_population_city:City = cities_of_highest_population()
        print(f'\t Neve: {highest_population_city.name}')
        print(f'\t Ország: {highest_population_city.country}')
        print(f'\t Lakosság: {highest_population_city.population}')
        print(f'A {count_cities_of_country("Kína")} legnagyobb kínai város össz lakossága: {sum_pop_country("Kína")}')


main()    