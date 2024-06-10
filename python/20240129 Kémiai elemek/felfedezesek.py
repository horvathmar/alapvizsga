class Adatok:
    def __init__(self, row: str) -> None:
        splitted = row.split(';')
        self.ev = splitted[0]
        self.nev = splitted[1]
        self.vegyjel = splitted[2]
        self.rendszam = splitted[3]
        self.felfedezo = splitted[4]