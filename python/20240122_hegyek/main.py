from peaks import *

def main():
    load_from_file('hegyekMo.txt')
    print(f'3. feladat: Hegycsúcsok száma: {len(list_of_peaks)} darab')
    print(f'4. feladat: Hegycsúcsok átlagos magassága: {avg_height()} m')
    print('A legmagasabb hegycsúcs adatai: ')
    highest = highest_peak()
    print(f'\tNév: {highest.name}')
    print(f'\tHegység: {highest.mountain}')
    print(f'\tMagasság: {highest.height}')
    height = int(input('6.feladat: Kérek egy magasságot: '))
    if exist_higher(height):
        print(f'\tVan {height} méternél magasabb hegycsúcs')
    else:
        print(f'\tNincs {height} méternél magasabb hegycsúcs')


    search_result = search_first_higher(height)
    if search_result != None:
        print(f'\tVan {height} méternél magasabb hegycsúcs {search_result.name}')
    else:
        print(f'\tNincs {height} méternél magasabb hegycsúcs')

    print(f'7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {count_height_over_foot(3000)}')
    print(f'9. feladat: buk-videk.txt')
    write_to_file('Bükk-vidék', 'bukk-videk.txt')

main()