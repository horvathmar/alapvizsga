from pilotak import *
def main():
    file_open('pilotak.csv')
    print(f'3. feladat: {len(pilotak_listaja)}')
    utolso_sor()
    tizenkilecedik_szazadi_pilotak()
    legkisebb_rajtszamu()
    azonos_rajtszam()

main()