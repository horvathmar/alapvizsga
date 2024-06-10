class Kuldetes:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(';')
        self.kod = splitted[0]
        self.datum = splitted[1]
        self.ursiklo_neve = splitted[2]
        self.nap = int(splitted[3])
        self.ora = int(splitted[4])
        self.legitamasz = splitted[5]
        self.legenyseg = int(splitted[6])
        self.ossz_ora = int(self.nap * 24 + self.ora)
        self.darabolt_datum = self.datum.split('.')
        self.evszam = int(self.darabolt_datum[0])