from pilota import Pilotak

pilotak_listaja : list[Pilotak] = []

def file_open(filename: str):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        pilotak_listaja.append(Pilotak(row))
    file.close()

def utolso_sor():
    for row in pilotak_listaja:
        if row.nev == pilotak_listaja[-1].nev:
            return print(f'4. feladat: {row.nev}')
        
def tizenkilecedik_szazadi_pilotak():
    # pilota_list_szul = []
    szul_dat = 1901
    for p in pilotak_listaja:
        if p.ev < szul_dat:
           print(f'{p.nev} ({p.szuletesi_datum})')
        
def legkisebb_rajtszamu():
    legkisebb_rajtszam = pilotak_listaja[0]
    for p in pilotak_listaja:
        if p.rajtszam > legkisebb_rajtszam.rajtszam and p.rajtszam != '':
            return print(f'6. feladat: {p.nemzetiseg}')
        
def azonos_rajtszam():
    # azonos_rajtszamuak = pilotak_listaja[0]
    # for p in pilotak_listaja:
    #     if p.rajtszam == azonos_rajtszamuak.rajtszam:
    #         print(p.rajtszam)
    pass