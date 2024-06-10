class Pilotak:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(';')
        self.nev = splitted[0]
        self.szuletesi_datum = splitted[1]
        self.nemzetiseg = splitted[2]
        self.rajtszam = splitted[3]

        darabolt = self.szuletesi_datum.split('.')
        self.ev = int(darabolt[0])