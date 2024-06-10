from competitiors import *

def main() -> None:
    load_from_file('fob2016.txt')
    print(f'3. feladat: Versenyzők száma: {len(competitors_list)}')
    # women = round(count("Noi")/len(competitors_list)*100, 2)
    women = count("Noi")/len(competitors_list)
    print(f'4. feladat: A női versenyzők aránya: {women:.2%}')

    # index = competitors_list[2].min_point()
    # print(competitors_list[2].points[index])
    print(competitors_list[2].min2_points())
    print('6. feladat: A bajnok női versenyző')
    winner_woman = winner('Noi')
    print(f'\tNév: {winner_woman.name}')
    print(f'\tEgyesület: {winner_woman.team}')
    print(f'\tÖsszpont: {winner_woman.total_points()}')
    save_to_file('osszpontFF.txt', 'Felnott ferfi')
main()