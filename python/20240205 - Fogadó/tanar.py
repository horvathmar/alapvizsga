import datetime

class Tanarok:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(' ')
        self.nev = f"{splitted[0]} {splitted[1]}"
        self.idopont = splitted[2]
        self.foglalas_ideje = splitted[3]

        foglalas_ideje, idopont = self.foglalas_ideje.strip('-')
    
        ev, honap, nap = foglalas_ideje.split('.')

        ora, perc = idopont.split(':')
        self.rogzites_datuma = datetime.datetime(int(ev), int(honap),int(nap), int(ora), int(perc))
