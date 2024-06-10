napok = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']

def mghszam(szo):
    mgh = 'aáeéiíoóöőuúüű'
    szamlalo = sum(1 for char in szo if char in mgh)
    return szamlalo

def legtobbmgh(napok):
    legtobbmgh = 0
    legnagyobb = ''
    for nap in napok:
        mghszama = mghszam(nap)
        if mghszama > legtobbmgh:
            legtobbmgh = mghszama
            legnagyobb = nap
    return legnagyobb

legtobbmghszam = legtobbmgh(napok)
print(f"A legtöbb magánhangzó ebben a napban van: {legtobbmghszam}")
